import sys
import os
sys.path.append( os.path.abspath("..") )
import myhdl
from myhdl import Signal, intbv, always, concat, always_comb
from src import des


#rx = Signal(intbv()[8:0])


@myhdl.block
def spi_slave(clk, miso, mosi, cs, rx):
	
	mosi_to_des = Signal(0)
	clk_to_des = Signal(0)
	enable_to_des = Signal(1)
	ddes =  des (clk_to_des, rx , mosi_to_des, enable_to_des )

	
	@always_comb
	def things():
		if(cs == 0):
			mosi_to_des.next = mosi
			clk_to_des.next = clk
		else:
			mosi_to_des.next = 0
			clk_to_des.next = 0
		enable_to_des.next =not cs
	
	
	return myhdl.instances()
