module tb_test_random;

wire c;
wire [0:0] l;

initial begin
    $to_myhdl(
        c,
        l
    );
end

test_random dut(
    c,
    l
);

endmodule
