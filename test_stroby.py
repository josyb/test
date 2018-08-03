
from __future__ import print_function

import myhdl
from myhdl import (block, Signal, ResetSignal, intbv, always,
                   instance, delay, StopSimulation)

# replace the following with from stroby import led_stroby
from fpga25_snip4 import led_stroby

num_led = 8

clock = Signal(False)
reset = ResetSignal(0, active=0, async=True)
leds = Signal(intbv(0)[num_led:])


@block
def test_random(clock, leds, reset):
    tbdut = led_stroby(clock, leds, reset)
    return tbdut


tr = test_random(clock, leds, reset)
# tr.run_sim(1000)
tr.convert('Verilog')
