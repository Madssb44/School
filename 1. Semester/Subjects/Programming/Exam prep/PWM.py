from machine import Pin, PWM
from time import sleep



ledrR= Pin(0, Pin.OUT)
ledgR=Pin(2, Pin.OUT)
ledyR=Pin(1, Pin.OUT)


ledrL = Pin(3, Pin.OUT)
ledyL = Pin(4, Pin.OUT)
ledgL = Pin(5, Pin.OUT)


pins = [
    Pin(2, Pin.OUT),  # A
    Pin(3, Pin.OUT),  # B
    Pin(4, Pin.OUT),  # C
    Pin(5, Pin.OUT),  # D
    Pin(6, Pin.OUT),  # E
    Pin(8, Pin.OUT),  # F
    Pin(7, Pin.OUT),  # G
    Pin(0, Pin.OUT)   # DP (not connected)
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



def main():
    blink()
    ledTest()

