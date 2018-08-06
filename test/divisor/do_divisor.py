import sys
import myhdl
import os
sys.path.append( os.path.abspath("../../src/") )
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from divisor import divisor



@block
def test_divisor(clk,out):
	clkdrv = ClkDriver(clk=clk, period=10)
	uut = divisor(clk_in=clk, division=3, clk_out=out)
	return uut, clkdrv

@block
def divider(clk,out):
	div = divisor(clk_in=clk, division=500000, clk_out=out)
	return div

if "--test" in str(sys.argv):
	do_test=True
else:
	do_test=False

clockrt = Signal(False)
clk_out = Signal(False)

if do_test:
	tr = test_divisor(clockrt, clk_out)
	tr.config_sim(trace=True)
	tr.run_sim(1000)
else:
	tr = divider(clock,clk_out)
	tr.convert('Verilog')
