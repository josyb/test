import sys
import myhdl
import os
sys.path.append( os.path.abspath("../../src/") )
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from wavegen import wavegen
from divisor import divisor

bus_width = 8

clock = Signal(False)
leds = Signal(intbv(0)[8:])
min_val = 0
max_val = 255

@block
def wavegenerator(
	# ~~~[Ports]~~~
	clock, 
	leds,
	# ~~~[Parameters]~~~
	speed=500000
):
	clk_div = Signal(False)
	div= divisor(clk_in=clock, division=speed,  clk_out= clk_div)
	wg = wavegen(clock=clk_div, out_val=leds, min_val=min_val, max_val=max_val, variation=1, bus_width=8)

	return wg, div

@block
def test_wavegenerator(clock, leds):
	clkdrv = ClkDriver(clk=clock, period=2)
	wg_uut = wavegenerator(clock=clock, leds=leds, speed=1)
	return wg_uut, clkdrv


if "--test" in str(sys.argv):
	do_test=True
else:
	do_test=False

if do_test:
	tr = test_wavegenerator(clock,leds)
	tr.config_sim(trace=True)
	tr.run_sim(1000)
else:
	tr = wavegenerator(clock, leds)
	tr.convert('Verilog',initial_values=True)
