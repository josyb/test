module tb_blinker;

reg clk;
wire [0:0] leds;

initial begin
    $from_myhdl(
        clk
    );
    $to_myhdl(
        leds
    );
end

blinker dut(
    clk,
    leds
);

endmodule
