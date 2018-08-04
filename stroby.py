

import myhdl
from myhdl import block, Signal, intbv
                 
from ClkDriver import ClkDriver

from fpga25_snip4 import led_stroby
from blinkled import blink
from shiftled import shift

num_led = 8
clock = Signal(False)
leds = Signal(intbv(0)[num_led:])


@block
def test_uut(c,l):

    clkdrv = ClkDriver(clk=c, period=10)
    tbdut = shift(c, l,num_led)
    return tbdut, clkdrv

@block
def trad(c,l):
    tbdut = shift(c, l,num_led)
    return tbdut

if 1:
    tr = test_uut(clock,leds)
    tr.config_sim(trace=True)
    tr.run_sim(1000)
else:
    tr = trad(clock,leds)
    tr.convert('Verilog')
