# test
Basic start with MyHDL

folders:

-src: you can find some block (or module) definition

-test: you can find usage for blocks, some tests are unitary, others use more blocks

makefile options:

    make upload    -> translate myHDL in verilog, sintesize, and load on fpga

    make test      -> run test in myHDL

    make clean     -> clean

this requires having icestorm http://www.clifford.at/icestorm/ and myhdl http://www.myhdl.org/start/installation.html installed
