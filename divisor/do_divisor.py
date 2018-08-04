import sys
import myhdl
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from divisor import divisor


clock = Signal(False)
clk_out = Signal(False)

@block
def test_divisor(clk,out):
    clkdrv = ClkDriver(clk=clk, period=10)
    uut = divisor(clk_in=clk, division=10, clk_out=out)
    return uut, clkdrv

@block
def divider(clk,out):
    div = divisor(clk_in=clk, division=500000, clk_out=out)
    return div

if "--test" in str(sys.argv):
    do_test=True
else:
    do_test=False

if do_test:
    tr = test_divisor(clock,pulse)
    tr.config_sim(trace=True)
    tr.run_sim(1000)
else:
    tr = divider(clock,clk_out)
    tr.convert('Verilog')
