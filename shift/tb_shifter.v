module tb_shifter;

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

shifter dut(
    clk,
    leds
);

endmodule
