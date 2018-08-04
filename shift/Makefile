tb: upload-tb

upload-tb: tb.bin
	sudo iceprog tb.bin

tb.bin: tb.txt
	icepack tb.txt tb.bin

tb.txt: tb.blif
	arachne-pnr -d 8k -p example-8k.pcf -o tb.txt tb.blif

tb.blif: shifter.v
	yosys -p "read_verilog shifter.v; synth_ice40 -blif tb.blif"

shifter.v: do_shift.py shift.py
	python do_shift.py

clean:
	rm tb.* *.v *.vcd

test: do_shift.py shift.py
	python do_shift.py --test
