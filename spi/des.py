
import myhdl
from myhdl import Signal, intbv, always, concat

#      deserializer
#       ---------
#       |       |
# rx  <-+-------+-< bit_in
#       |       |
#       ---------

#TODO MSB/LSB  
#shift << or >>
#concatenation in head or tail

#TODO CPHA/CPOL
#CPOL first or second edge




@myhdl.block
def des(
	# ~~~[Ports]~~~
	clock,	#
	rx,	#
	bit_in,	#
	reset,	#
	# ~~~[Parameters]~~~
	size=8
):
	assert len(rx) == size
	# serialization register
	ser_reg = Signal(intbv(0)[size:])
	bitcnt = Signal(intbv(0, min=0, max=size+1))

	@always(clock.posedge)
	def deserialization():
		if(reset == 0):
			ser_reg.next = ((ser_reg<<1) | bit_in) & 0xFF 
			bitcnt.next = bitcnt + 1
			if bitcnt == (size-1):
				rx.next=((ser_reg<<1) | bit_in) & 0xFF
				bitcnt.next = 0
		else:		
			ser_reg.next=0
			rx.next=0
			bitcnt.next = 0

	return myhdl.instances()
