module tb_trad;

reg c;
wire [7:0] l;

initial begin
    $from_myhdl(
        c
    );
    $to_myhdl(
        l
    );
end

trad dut(
    c,
    l
);

endmodule
