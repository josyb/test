import sys
import myhdl
import os
sys.path.append( os.path.abspath("../../src/") )

from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from divisor import divisor

leds = Signal(intbv(0)[8:])

@block
def divider(clock,leds,division=5000000):
	div = divisor(clk_in=clock, clk_out=leds, division=division)
	return div

@block
def test_divider(clock,out):
	clkdrv = ClkDriver(clk=clock, period=10)
	uut = divider(clock=clock, division=3, leds=out)
	return uut, clkdrv



if "--test" in str(sys.argv):
	do_test=True
else:
	do_test=False

clock = Signal(False)

clk_out = Signal(False)

if do_test:
	tr = test_divider(clock, clk_out)
	tr.config_sim(trace=True)
	tr.run_sim(1000)
else:
	tr = divider(clock,leds)
	tr.convert('Verilog',initial_values=True)
