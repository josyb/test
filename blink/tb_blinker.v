module tb_blinker;

reg clk;
wire [7:0] leds;

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
