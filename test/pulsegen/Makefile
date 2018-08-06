upload: tb.bin
	sudo iceprog tb.bin

tb.bin: tb.txt
	icepack tb.txt tb.bin

tb.txt: tb.blif
	arachne-pnr -d 8k -p ../../conf_pcf/ICE40H8KBreakoutBoard.pcf  -o tb.txt tb.blif

tb.blif: pulsegenerator.v
	yosys -p "read_verilog pulsegenerator.v; synth_ice40 -blif tb.blif"

pulsegenerator.v: do_pulsegen.py
	python do_pulsegen.py

clean:
	rm tb.* *.v *.vcd *.pyc

test: do_pulsegen.py
	python do_pulsegen.py --test
