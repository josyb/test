import sys
import os
sys.path.append( os.path.abspath("../../") )
import myhdl
from myhdl import StopSimulation, Signal, intbv, block, now, instance, delay
from src import ser, spi_slave, ClkDriver

clock = Signal(0)
sck = Signal(0)
mosi = Signal(0)
miso = Signal(0)
cs = Signal(1)
out_byte = Signal(intbv(0)[8:])
in_byte = Signal(intbv(0)[8:])
enable = Signal(0)

@block
def test_ss(clock, mosi, cs, out):
	clkdrv = ClkDriver(clock,period=10)
	ss = spi_slave (clock, miso, mosi, cs, out_byte)
	tser = ser(clock,in_byte,mosi,enable )	


	@instance
	def tbstim():
		yield delay(15)
		enable.next=1
		in_byte.next=42
		cs.next=0
		yield delay(90)
		cs.next=1
		enable.next=0
		assert out_byte == 42 
		yield delay(100)
		raise StopSimulation

	return clkdrv, ss, tser, tbstim

tr = test_ss(clock, mosi, cs, out_byte)
tr.config_sim(trace=True)
tr.run_sim(1000)
