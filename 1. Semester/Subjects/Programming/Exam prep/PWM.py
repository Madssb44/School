from machine import Pin, PWM
from time import sleep



ledrL= Pin(0, Pin.OUT)
ledgL=Pin(2, Pin.OUT)
ledyL=Pin(1, Pin.OUT)

led_PWM = PWM(ledrL)
led_PWM.freq(8)


ledrR = Pin(3, Pin.OUT)
ledyR = Pin(4, Pin.OUT)
ledgR = Pin(5, Pin.OUT)


pins = [
    Pin(8, Pin.OUT),  # A
    Pin(9, Pin.OUT),  # B
    Pin(10, Pin.OUT),  # C
    Pin(12, Pin.OUT),  # D
    Pin(13, Pin.OUT),  # E
    Pin(15, Pin.OUT),  # F
    Pin(14, Pin.OUT),  # G
    Pin(11, Pin.OUT)   # DP (not connected)
]


digits = [
    [0, 0, 0, 0, 0, 0, 1, 1], # 0
    [1, 0, 0, 1, 1, 1, 1, 1], # 1
    [0, 0, 1, 0, 0, 1, 0, 1], # 2 
    [0, 0, 0, 0, 1, 1, 0, 1], # 3
    [1, 0, 0, 1, 1, 0, 0, 1], # 4
    [0, 1, 0, 0, 1, 0, 0, 1], # 5
    [0, 1, 0, 0, 0, 0, 0, 1], # 6
    [0, 0, 0, 1, 1, 1, 1, 1], # 7
    [0, 0, 0, 0, 0, 0, 0, 1], # 8
    [0, 0, 0, 1, 1, 0, 0, 1], # 9
]


def reset():
    """Turns off all segments on the 7-segment display."""
    for pin in pins:
        pin.value(1)


def blink():
    for pin in pins:
        pin.on()
        sleep(1)

    for pin in pins:
        pin.off()

def ledTest():
    ledgL.on()
    ledyL.on()
    ledrL.on()
    ledgR.on()
    ledyR.on()
    ledrR.on()
    sleep(2)

    ledgL.off()
    ledyL.off()
    ledrL.off()
    ledgR.off()
    ledyR.off()
    ledrR.off()

def PWMTest():
    duty_step = 50000
    for i in range(100):
        led_PWM.duty_u16(duty_step)
        sleep(0.05)
    

def main():
    #blink()
    #ledTest()
    PWMTest()


main()
