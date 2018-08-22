import sys
import os
sys.path.append( os.path.abspath("../../src/") )
import myhdl
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from pulsegen import pulsegen
from wavegen import wavegen
from divisor import divisor

clock = Signal(False)
pulse = Signal(False)

width=32

@block
def wavepulser(
	# ~~~[Ports]~~~
	clock,
	out,
	# ~~~[Parameters]~~~
	frequency_min =2000,
	frequency_max =20000,
	duration = 100,
	wavespeed = 50000,
	wavevariation=40
):
	
	frequency_mean=(frequency_min+frequency_max)/2

	freq = Signal(intbv(frequency_min ,max=10000000)[width:])
	dur = Signal (intbv(duration ,max=10000000)[width:])
	clk_div = Signal(False)
	pg = pulsegen (clock, freq, dur, out)
	div = divisor (clk_in=clock, division=wavespeed,  clk_out= clk_div)
	wg = wavegen (clk_div, out_val=freq, min_val=frequency_min, max_val=frequency_max, start=frequency_mean, variation=wavevariation)
	return wg, pg, div

@block
def test_wavepulser(clock,out):
	clkdrv = ClkDriver(clk=clock, period=10)
	wp=wavepulser(clock=clock, out=out, frequency_min=2,frequency_max=8, duration=1, wavespeed=30, wavevariation=1)
	return wp, clkdrv

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
	tr.convert('Verilog',initial_values=True)
