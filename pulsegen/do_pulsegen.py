import sys
import myhdl
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from pulsegen import pulsegen


num_led = 8
clock = Signal(False)
leds = Signal(intbv(0)[num_led:])

@block
def test_pulsegenerator(clk,leds):
    clkdrv = ClkDriver(clk=clk, period=10)
    tbdut = blink(clk, leds, num_led=num_led, cnt_max=5)
    return tbdut, clkdrv

@block
def pulsegenerator(clk,leds):
    tbdut = pulsegen(clk, leds, num_led)
    return tbdut

if "--test" in str(sys.argv):
    do_test=True
else:
    do_test=False

if do_test:
    tr = test_pulsegenerator(clock,leds)
    tr.config_sim(trace=True)
    tr.run_sim(1000)
else:
    tr = pulsegenerator(clock,leds)
    tr.convert('Verilog')
