import myhdl
from myhdl import StopSimulation, Signal, intbv, block, always
from ser import ser
from ClkDriver import ClkDriver 

clock = Signal(0)
tx = Signal(intbv(42)[8:])
out = Signal(0)

@block
def test(out):
	clkdrv = ClkDriver(clock,period=10)
	ss = ser (clock, tx, out)

	@always(clock.posedge)
	def init():
		tx.next=42

	return clkdrv, ss, init

tr = test(out)
tr.config_sim(trace=True)
tr.run_sim(1000)

