import sys
import os
sys.path.append( os.path.abspath("../../src/") )
import myhdl
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
#from fpga25_snip4 import led_stroby
from shift import shift

num_led = 8
clock = Signal(False)
leds = Signal(intbv(0)[num_led:])


@block
def test_shifter(clock,leds):
    clkdrv = ClkDriver(clock, period=10)
    tbdut = shift(clock, leds, num_led=num_led, cnt_max=5)
    return tbdut, clkdrv

@block
def shifter(clock,leds):
    tbdut = shift(clock, leds, num_led)
    return tbdut

if "--test" in str(sys.argv):
    do_test=True
else:
    do_test=False

if do_test:
    tr = test_shifter(clock,leds)
    tr.config_sim(trace=True)
    tr.run_sim(1000)
else:
    tr = shifter(clock,leds)
    tr.convert('Verilog',initial_values=True)
