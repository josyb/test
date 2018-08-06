import sys
import os
sys.path.append( os.path.abspath("../../src/") )

import myhdl
from myhdl import block, Signal, intbv, always_comb

from ClkDriver import ClkDriver
from blink import blink
from divisor import divisor

num_led = 8
clock = Signal(False)
leds = Signal(intbv(0)[num_led:])

@block
def test_blinker(clk,leds):
	clkdrv = ClkDriver(clk=clk, period=10)
	tbdut = blink(clk, leds, num_led=num_led, cnt_max=5)
	return tbdut, clkdrv

@block
def blinker(clk,leds):
	#tbdut = blink(clk, leds, num_led)
	blink_signal = Signal(intbv(0)[1:])
	blink_uut = divisor(clk_in=clk, clk_out= blink_signal, division = 5000000)

	
	@always_comb
	def map_N_led():
		for i in range(0,8):
			if(i < num_led):
				leds[i].next = blink_signal
			else:
				leds[i].next = 0

	return blink_uut, map_N_led

if "--test" in str(sys.argv):
	do_test=True
else:
	do_test=False

if do_test:
	tr = test_blinker(clock,leds)
	tr.config_sim(trace=True)
	tr.run_sim(1000)
else:
	tr = blinker(clock,leds)
	tr.convert('Verilog',initial_values=True)
