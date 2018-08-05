tb: upload-tb

upload-tb: tb.bin
	sudo iceprog tb.bin

tb.bin: tb.txt
	icepack tb.txt tb.bin

tb.txt: tb.blif
	arachne-pnr -d 8k -p example-8k.pcf -o tb.txt tb.blif

tb.blif: blinker.v
	yosys -p "read_verilog blinker.v; synth_ice40 -blif tb.blif"

blinker.v: do_blink.py blink.py
	python do_blink.py

clean:
	rm tb.* *.v *.vcd *.pyc


test: do_blink.py blink.py
	python do_blink.py --test
