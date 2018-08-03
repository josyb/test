
8k: upload-8k 

upload-8k: example-8k.bin
	sudo iceprog example-8k.bin && rm example-8k.bin

example-8k.bin: example-8k.txt
	icepack example-8k.txt example-8k.bin && rm example-8k.txt

example-8k.txt: example-8k.blif
	arachne-pnr -d 8k -p example-8k.pcf -o example-8k.txt example-8k.blif && rm example-8k.blif

example-8k.blif: example-8k.v
	yosys -p "read_verilog example-8k.v; synth_ice40 -blif example-8k.blif"


tb: upload-tb 

upload-tb: tb.bin
	sudo iceprog tb.bin 

tb.bin: tb.txt
	icepack tb.txt tb.bin

tb.txt: tb.blif
	arachne-pnr -d 8k -p example-8k.pcf -o tb.txt tb.blif 

tb.blif: test_random.v
	yosys -p "read_verilog test_random.v; synth_ice40 -blif tb.blif"
