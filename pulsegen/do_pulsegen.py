import sys
import myhdl
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from pulsegen import pulsegen

clock = Signal(False)
pulse = Signal(False)
width = 32

@block
def test_pulsegenerator(clk,out):
	freq = Signal(intbv(30,min=0,max=50))
	dur = Signal(intbv(12,min=0,max=20))
	clkdrv = ClkDriver(clk=clk, period=10)
	uut = pulsegen(clk, freq, dur, pulse)
	return uut, clkdrv

@block
def pulsegenerator(clk,out):
	freq = Signal(intbv(5000000,max=10000000)[width:])
	dur = Signal (intbv(1000000,max=10000000)[width:])
	pulsegener = pulsegen(clk, freq, dur, pulse)
	return pulsegener

if "--test" in str(sys.argv):
	do_test=True
else:
	do_test=False

if do_test:
	tr = test_pulsegenerator(clock,pulse)
	tr.config_sim(trace=True)
	tr.run_sim(1000)
else:
	tr = pulsegenerator(clock,pulse)
	tr.convert('Verilog')
