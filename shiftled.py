from myhdl import Signal, intbv, always, always_comb, block, now

@block
def shift(
  # ~~~[Ports]~~~
  clock,                 # input : system sync clock
  led,                   # output : to IO ports drive LEDs
  # ~~~[Parameters]~~~
  # The number of dummy LEDS on each side
  num_led
):


    cnt_max = 5#000000#int(clock_frequency * led_rate)   
    
    # Declare the internal Signals in our design
    led_mem = Signal(intbv(1)[num_led:0])
    #print(led_mem.max)
    clk_cnt = Signal(intbv(0, min=0, max=cnt_max))
    strobe = Signal(False)
    ltr = Signal(True)

    @always(clock.posedge)
    def beh_strobe():
        if clk_cnt >= cnt_max-1:
            clk_cnt.next = 0
            print ("%s led change!%s"% (now(),str(led_mem)))
            if ltr:
                led_mem.next=led_mem<<1
            else:
                led_mem.next=led_mem>>1
            if led_mem == 1<<1:
                ltr.next=1
                print ("%s dir change!  go 1"%now())
            if led_mem == (1<<(num_led-2)):
                ltr.next=0
                print ("%s dir change!  go 0"%now())

        else:
            clk_cnt.next = clk_cnt + 1


    @always_comb
    def beh_map_output():
        led.next = led_mem
        
    return beh_strobe, beh_map_output
