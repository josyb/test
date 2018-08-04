clean:
	rm tb.blif  tb.txt tb.bin

tb: upload-tb

upload-tb: tb.bin
	sudo iceprog tb.bin

tb.bin: tb.txt
	icepack tb.txt tb.bin

tb.txt: tb.blif
	arachne-pnr -d 8k -p example-8k.pcf -o tb.txt tb.blif

tb.blif: test_random.v
	yosys -p "read_verilog trad.v; synth_ice40 -blif tb.blif"
