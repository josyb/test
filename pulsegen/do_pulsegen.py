import sys
import myhdl
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from pulsegen import pulsegen


num_led = 8
clock = Signal(False)
pulse = Signal(False)
freq = Signal(intbv(30,max=50))
dur = Signal(intbv(12,max=20))

@block
def test_pulsegenerator(clk,out):
    clkdrv = ClkDriver(clk=clk, period=10)
    uut = pulsegen(clk, freq, dur, pulse)
    return uut, clkdrv

@block
def pulsegenerator(clk,leds):
    pulsegen = pulsegen(clk, freq, dur, pulse)
    return pulsegen

if "--test" in str(sys.argv):
    do_test=True
else:
    do_test=False

if do_test:
    tr = test_pulsegenerator(clock,pulse)
    tr.config_sim(trace=True)
    tr.run_sim(1000)
else:
    tr = pulsegenerator(clock,leds)
    tr.convert('Verilog')
