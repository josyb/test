from myhdl import Signal, intbv, always, always_comb, block, now

@block
def divisor(
	# ~~~[Ports]~~~
	clk_in,		# input  : clock
	clk_out,	# output  : one pulse will start every frequence clock cycles

	# ~~~[Parameters]~~~
	division = 100
):
	div_mem = Signal(intbv(0)[1:0])
	clk_cnt = Signal(intbv(0, min=0, max=division))

	@always(clk_in.posedge)
	def beh_strobe():
		#print ("%s posedge "%(now()))
		if clk_cnt >= division-1:
			div_mem.next = not div_mem
			clk_cnt.next = 0
		else:
			clk_cnt.next = clk_cnt + 1

	@always_comb
	def beh_map_output():
		clk_out.next = div_mem

	return beh_strobe, beh_map_output
