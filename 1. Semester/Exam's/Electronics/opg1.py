from machine import Pin, PWM
from time import sleep_ms


ledrL= Pin(0, Pin.OUT)
ledgL=Pin(2, Pin.OUT)
ledyL=Pin(1, Pin.OUT)


ledrR = Pin(3, Pin.OUT)
ledyR = Pin(4, Pin.OUT)
ledgR = Pin(5, Pin.OUT)



gR = PWM(ledgR)
yR = PWM(ledyR)
rR = PWM(ledrR)
gL = PWM(ledgL)
yL = PWM(ledyL)
rL = PWM(ledrL)






while True:
    gR.freq(800)
    gL.freq(800)
    gL.duty_u16(0)
    gR.duty_u16(2**16)
    sleep_ms(500)
    gR.duty_u16(0)
    gL.duty_u16(2**16)
    sleep_ms(500)


