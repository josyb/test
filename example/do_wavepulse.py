import sys
import myhdl
from myhdl import block, Signal, intbv

from pulsegen import pulsegen
from wavegen import wavegen
from divisor import divisor

clock = Signal(False)
pulse = Signal(False)


@block
def test_pulsegenerator(clk,out):
	freq = Signal(intbv(30,max=50))
	dur = Signal(intbv(12,max=20))
	clk_div = Signal(False)
	pg = pulsegen(clk, freq, dur, out)
	div = divisor(clk_in=clk, division=15 ,clk_out= clk_div)
	wg = wavegen(clk_div,freq,min_val=20, max_val=50,start=30)
	return pg, div, wg

if do_test:
	tr = test_pulsegenerator(clock,pulse)
	tr.config_sim(trace=True)
	tr.run_sim(1000)
else:
	tr = pulsegenerator(clock,leds)
	tr.convert('Verilog')
