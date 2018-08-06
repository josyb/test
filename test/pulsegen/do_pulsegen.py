import sys
import os
sys.path.append( os.path.abspath("../../src/") )
import myhdl
from myhdl import block, Signal, intbv, always_comb

from ClkDriver import ClkDriver
from pulsegen import pulsegen

clock = Signal(False)
pulse = Signal(False)

width = 32
leds = Signal(intbv(0)[8:])

@block
def pulsegenerator(clock, leds, frequence=5000000, duration=1000000, num_out=8):
	pulse_signal= Signal(intbv(0)[1:])

	freq = Signal(intbv(frequence, max=10000000)[width:])
	dur = Signal (intbv(duration, max=10000000)[width:])
	pg = pulsegen(clock, freq, dur, pulse_signal)

	@always_comb
	def map_pulse():
		for i in range(0,num_out):
			leds.next[i] = pulse_signal				
	return pg, map_pulse



@block
def test_pulsegenerator(clock,leds):
	clkdrv = ClkDriver(clk=clock, period=10)
	uut = pulsegenerator(clock, leds, frequence=30, duration=12)
	return uut, clkdrv


if "--test" in str(sys.argv):
	do_test=True
else:
	do_test=False

if do_test:
	tr = test_pulsegenerator(clock,leds)
	tr.config_sim(trace=True)
	tr.run_sim(1000)
else:
	tr = pulsegenerator(clock,leds)
	tr.convert('Verilog',initial_values=True)
