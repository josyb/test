// File: test_random.v
// Generated by MyHDL 0.10
// Date: Fri Aug  3 11:07:59 2018


`timescale 1ms/10us


module test_random (
    input clock,
    output LED1,
    output LED2,
    output LED3,
    output LED4,
    output LED5,
    output LED6,
    output LED7,
    output LED8
);


//wire [7:0] leds;
//wire clock;
reg led_stroby0_left_not_right;
reg [13:0] led_stroby0_clk_cnt;
reg led_stroby0_strobe;
reg [7:0] led_stroby0_led_bit_mem;


always @(posedge clock) begin: TEST_RANDOM_LED_STROBY0_BEH_STROBE
    if (($signed({1'b0, led_stroby0_clk_cnt}) >= (100 - 1))) begin
        led_stroby0_clk_cnt <= 0;
        led_stroby0_strobe <= 1'b1;
    end
    else begin
        led_stroby0_clk_cnt <= (led_stroby0_clk_cnt + 1);
        led_stroby0_strobe <= 1'b0;
    end
    if (led_stroby0_strobe) begin
        if (led_stroby0_led_bit_mem[7]) begin
            led_stroby0_led_bit_mem <= 64;
            led_stroby0_left_not_right <= 1'b0;
            $write("ltr");
            $write("\n");
        end
        else if (led_stroby0_led_bit_mem[0]) begin
            led_stroby0_led_bit_mem <= 2;
            led_stroby0_left_not_right <= 1'b1;
            $write("rtl");
            $write("\n");
        end
        else begin
            if (led_stroby0_left_not_right) begin
                led_stroby0_led_bit_mem <= (led_stroby0_led_bit_mem << 1);
            end
            else begin
                led_stroby0_led_bit_mem <= (led_stroby0_led_bit_mem >>> 1);
            end

        end
    end
end


assign {LED1, LED2, LED3, LED4, LED5, LED6, LED7, LED8} = led_stroby0_led_bit_mem;

endmodule