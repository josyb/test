import sys
import os
sys.path.append( os.path.abspath("../../src/") )

import myhdl
from myhdl import block, Signal, intbv, always_comb

from ClkDriver import ClkDriver

from divisor import divisor

num_led = 5
clock = Signal(False)
leds = Signal(intbv(0)[8:])

@block
def blinker(
	# ~~~[Ports]~~~
	clk,
	leds,
	# ~~~[Parameters]~~~
	blink_clock = 5000000,
	num_led = 1
):

	blink_signal = Signal(intbv(0)[1:])
	blink_uut = divisor(clk_in=clk, clk_out= blink_signal, division = blink_clock)
	
	@always_comb
	def map_N_led():
		for i in range(0,8):
			if(i < num_led):
				leds.next[i] = blink_signal				
			else:
				leds.next[i] = 0

	return blink_uut, map_N_led

@block
def test_blinker(clk,leds):
	clkdrv = ClkDriver(clk=clk, period=10)
	blink_uut = blinker( clk, leds, num_led = num_led, blink_clock = 5 )
	return blink_uut, clkdrv


if "--test" in str(sys.argv):
	do_test=True
else:
	do_test=False

if do_test:
	is_testing=1
	tr = test_blinker(clock,leds)
	tr.config_sim(trace=True)
	tr.run_sim(1000)
else:
	is_testing=0
	tr = blinker(clock,leds,num_led=num_led)
	tr.convert('Verilog',initial_values=True)
