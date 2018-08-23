import sys
import os
sys.path.append( os.path.abspath("../../") )
import myhdl
from myhdl import StopSimulation, Signal, intbv, block, always, instance, delay
from src import ser, des, ClkDriver

clock = Signal(0)
tx = Signal(intbv(0)[8:])
rx = Signal(intbv(0)[8:])
out = Signal(0)
enable = Signal (0)

@block
def test(out):
	clkdrv = ClkDriver(clock,period=10)
	ts = ser (clock, tx, out,enable)
	td= des (clock, rx, out,enable)

	@instance
	def tbstim():
		yield delay(15)
		enable.next=1
		tx.next=42
		yield delay(90)
		enable.next=0
		assert rx == 42

		yield delay(15)
		enable.next=1
		tx.next=98
		yield delay(70)
		tx.next=23
		yield delay(20)		
		assert rx == 98

		
		yield delay(90)
		assert rx == 23
		enable.next=0
		yield delay(100)
		raise StopSimulation


	return clkdrv, ts, td, tbstim

tr = test(out)
tr.config_sim(trace=True)
tr.run_sim(1000)
