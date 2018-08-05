import sys
import myhdl
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from blink import blink


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
    tbdut = blink(clk, leds, num_led)
    return tbdut

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
    tr.convert('Verilog')
