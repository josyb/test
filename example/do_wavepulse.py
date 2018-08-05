import sys
import myhdl
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from pulsegen import pulsegen
from wavegen import wavegen
from divisor import divisor

clock = Signal(False)
pulse = Signal(False)

width=20
@block
def wavepulser(clk,out):
	freq = Signal(intbv(5000000,max=10000000)[width:])
	dur = Signal (intbv(1000000,max=10000000)[width:])
	clk_div = Signal(False)
	pg = pulsegen(clk, freq, dur, out)
	#div = divisor(clk_in=clk, division=30 ,clk_out= clk_div)
	#wg = wavegen(clk_div,freq,min_val=2, max_val=10,start=3)
	return pg#, div, wg

@block
def test_wavepulser(clk,out):
	clkdrv = ClkDriver(clk=clk, period=10)
	freq = Signal(intbv(3,max=50))
	dur = Signal(intbv(1,max=20))
	clk_div = Signal(False)
	pg = pulsegen(clk, freq, dur, out)
	div = divisor(clk_in=clk, division=30 ,clk_out= clk_div)
	wg = wavegen(clk_div,freq,min_val=2, max_val=10,start=3)
	return pg, div, wg, clkdrv

if "--test" in str(sys.argv):
	do_test=True
else:
	do_test=False

if do_test:
	tr = test_wavepulser(clock,pulse)
	tr.config_sim(trace=True)
	tr.run_sim(10000)
else:
	tr = wavepulser(clock,pulse)
	tr.convert('Verilog')
