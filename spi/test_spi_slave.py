import myhdl
from myhdl import StopSimulation, Signal, intbv, block, now
from spi_slave import spi_slave
from ClkDriver import ClkDriver 

clock = Signal(0)
sck = Signal(0)
mosi = Signal(0)
miso = Signal(0)
cs = Signal(1)
out_bute = Signal(intbv(0)[8:])
in_byte = Signal(intbv(0)[8:])
enable = Signal(0)

@block
def test_ss(clock, mosi, cs, out):
	clkdrv = ClkDriver(clock,period=10)
	ss = spi_slave (clock, miso, mosi, cs, out_byte)
	tser = ser(clock,in_byte,mosi,enable )
	return clkdrv, ss, tser

tr = test_ss(clock, mosi, cs, out_byte)
tr.config_sim(trace=True)
tr.run_sim(1000)
