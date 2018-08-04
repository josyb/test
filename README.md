# test
Basic start with MyHDL

blink folder blink all leds on ice40 H8X Breakout Board

editing num_led in do_blink.py you can choose how many of them, from 2 to 8 (not working with only 1)

shifter folder "should" blink one led a time, shifting it left and right, still not working though

makefile options:

    make tb    -> translate myHDL in verilog, sintesize, and load on fpga

    make test  -> run test in myHDL

    make clean -> clean

