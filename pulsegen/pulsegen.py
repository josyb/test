from myhdl import Signal, intbv, always, always_comb, block, now

@block
def pulsegen(
  # ~~~[Ports]~~~
  clock,                 # input : system sync clock
  led,                   # output : to IO ports drive LEDs
  # ~~~[Parameters]~~~
  num_led,
  cnt_max = 5000000#int(clock_frequency * led_rate)

):
    led_mem = Signal(intbv(0)[num_led:0])
    clk_cnt = Signal(intbv(0, min=0, max=cnt_max))
    strobe = Signal(False)

    @always(clock.posedge)
    def beh_strobe():
        if clk_cnt >= cnt_max-1:
            clk_cnt.next = 0
            strobe.next = not strobe
            if strobe:
                led_mem.next=0
                print ("%s change!%s"% (now(),str(led_mem)))
            else:
                led_mem.next=led_mem.max-1
                print ("%s change!%s"% (now(),str(led_mem)))
        else:
            clk_cnt.next = clk_cnt + 1

    @always_comb
    def beh_map_output():
        led.next = led_mem

    return beh_strobe, beh_map_output
