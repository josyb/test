tb: upload-tb

upload-tb: tb.bin
	sudo iceprog tb.bin

tb.bin: tb.txt
	icepack tb.txt tb.bin

tb.txt: tb.blif
	arachne-pnr -d 8k -p example-8k.pcf -o tb.txt tb.blif

tb.blif: wavepulser.v
	yosys -p "read_verilog wavepulser.v; synth_ice40 -blif tb.blif"

wavepulser.v: do_wavepulse.py
	python do_wavepulse.py

clean:
	rm tb.* *.v *.vcd *.pyc


test: do_wavepulse.py
	python do_wavepulse.py --test
