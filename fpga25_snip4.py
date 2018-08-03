
from myhdl import Signal, intbv, always, always_comb, block


@block
def led_stroby(
  # ~~~[Ports]~~~
  clock,  # input : system sync clock
  led,  # output : to IO ports drive LEDs
  reset=None,  # input : reset
  # ~~~[Parameters]~~~
  # The number of dummy LEDS on each side
):

    # Number of LEDs
    led_bank = len(led)
#     print("led bank=",led_bank)
    # Need to calculate some constants.  Want the value to
    # be an integer (non-fractional value only whole number)
    cnt_max = 1000000  # int(clock_frequency * led_rate)

    # Some useful definitions
    mb = led_bank
    lsb, msb = 0, mb - 1
    msb_reverse_val = (1 << mb - 2)
    lsb_reverse_val = 2

    # Declare the internal Signals in our design
    led_bit_mem = Signal(intbv(1)[mb:])
    left_not_right = Signal(True)
    clk_cnt = Signal(intbv(0, min=0, max=cnt_max))
    strobe = Signal(False)

    @always(clock.posedge)
    def beh_strobe():
        # print ("%s posedge!"% now())
        # Generate the strobe event, use the "greater
        # than" for initial condition cases.  Count the
        # number of clock ticks that equals the LED strobe rate
        if clk_cnt >= cnt_max - 1:
            clk_cnt.next = 0
            strobe.next = True
        else:
            clk_cnt.next = clk_cnt + 1
            strobe.next = False

        # Describe the strobing, note the following always
        # changes direction and "resets" when either the lsb
        # or msb is set.  This handles our initial condition
        # as well.
        if strobe:
            if led_bit_mem[msb]:
                led_bit_mem.next = msb_reverse_val
                left_not_right.next = False
#                 print ("ltr")
            elif led_bit_mem[lsb]:
                led_bit_mem.next = lsb_reverse_val
                left_not_right.next = True
#                 print ("rtl")
            else:
                if left_not_right:
                    led_bit_mem.next = led_bit_mem << 1
                else:
                    led_bit_mem.next = led_bit_mem >> 1
#                 print("%s moving %s" %(now(), str(led_bit_mem)))

    @always_comb
    def beh_map_output():
        led.next = led_bit_mem

    return beh_strobe, beh_map_output
