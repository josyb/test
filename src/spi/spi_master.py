import sys
import os
sys.path.append( os.path.abspath("../") )
import myhdl
from myhdl import Signal, intbv, always, always_comb,block
from src import des


#rx = Signal(intbv()[8:0])


@block
def spi_master(clk, miso, mosi, cs, rx):
	
	mosi_to_ser = Signal(0)
	clk_to_ser = Signal(0)
	rst_to_ser = Signal(1)
	dser = des (clk_to_des, rx , mosi_to_des, rst_to_des )

	@always(clk.posedge)
	def boh():
		pass	


	@always_comb
	def logic():
		if(cs == 0):
			mosi_to_des.next = mosi
			clk_to_des.next = clk
		else:
			mosi_to_des.next = 0
			clk_to_des.next = 0
		rst_to_des.next =cs
	
	
	return logic, ddes, boh
