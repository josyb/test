import sys
import myhdl
from myhdl import block, Signal, intbv

from ClkDriver import ClkDriver
from wavegen import wavegen

bus_width = 12

clock = Signal(False)
wave = Signal(intbv(0)[bus_width:0])
min_val = Signal(intbv(20)[bus_width:0])
max_val = Signal(intbv(25)[bus_width:0])

@block
def test_wavegenerator(clk,min_val, max_val, wave, bus_width, start=24):
    clkdrv = ClkDriver(clk=clk, period=10)
    uut = wavegen(clk, min_val, max_val, wave)
    return uut, clkdrv

@block
def wavegenerator(clk,min_val, max_val, wave):
    wavegene = wavegen(clk, min_val, max_val, wave)
    return wavegene

if "--test" in str(sys.argv):
    do_test=True
else:
    do_test=False

if do_test:
    tr = test_wavegenerator(clock,min_val, max_val, wave)
    tr.config_sim(trace=True)
    tr.run_sim(1000)
else:
    tr = wavegenerator(clock, min_val, max_val, wave)
    tr.convert('Verilog')
