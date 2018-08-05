from myhdl import Signal, intbv, always, always_comb, block, now

@block
def wavegen(
	# ~~~[Ports]~~~
	clock,		# input  : clock
	out_val,	# output : the output with the pulse
	# ~~~[Parameters]~~~
	min_val,	# input  : one pulse will start every frequence clock cycles
	max_val,	# input  : every pulse will last duration clock cycles
	bus_width = 32,
	start = 0,
	count = 10000 
):
	val_mem = Signal(intbv(start, max=max_val)[bus_width:0])
	up_or_down = Signal(intbv(1,max=2)[1:0])
	clk_cnt = Signal(intbv(0, min=0)[bus_width:0])


	@always(clock.posedge)
	def beh_strobe():
		
		if clk_cnt >= count:
			if up_or_down:
				val_mem.next = val_mem+20
			else:
				val_mem.next = val_mem-20	
			clk_cnt.next = 0
		else:
			clk_cnt.next = clk_cnt + 1

		if val_mem >= max_val:
			up_or_down.next = 0
		if val_mem <= min_val:
			up_or_down.next = 1
	@always_comb
	def beh_map_output():
		out_val.next = val_mem

	return beh_strobe, beh_map_output