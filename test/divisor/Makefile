upload: tb.bin
	sudo iceprog tb.bin

tb.bin: tb.txt
	icepack tb.txt tb.bin

tb.txt: tb.blif
	arachne-pnr -d 8k -p ../../conf_pcf/ICE40H8KBreakoutBoard.pcf -o tb.txt tb.blif

tb.blif: divider.v
	yosys -p "read_verilog divider.v; synth_ice40 -blif tb.blif"

divider.v: do_divisor.py
	python do_divisor.py

clean:
	rm tb.* *.v *.vcd *.pyc


test: do_divisor.py 
	python do_divisor.py --test
