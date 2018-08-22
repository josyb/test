import myhdl
from myhdl import StopSimulation, Signal, intbv, block, always
from ser import ser
from des import des
from ClkDriver import ClkDriver 

clock = Signal(0)
tx = Signal(intbv(42)[8:])
rx = Signal(intbv(0)[8:])
out = Signal(0)

@block
def test(out):
	clkdrv = ClkDriver(clock,period=10)
	ts = ser (clock, tx, out)
	td= des (clock, rx, out)

	return clkdrv, ts, td

tr = test(out)
tr.config_sim(trace=True)
tr.run_sim(1000)
