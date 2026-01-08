from machine import Pin, PWM
from time import sleep_ms


ledrL= Pin(0, Pin.OUT)
ledgL=Pin(2, Pin.OUT)
ledyL=Pin(1, Pin.OUT)


ledrR = Pin(3, Pin.OUT)
ledyR = Pin(4, Pin.OUT)
ledgR = Pin(5, Pin.OUT)



gR = PWM(ledgR)
#yR = PWM(ledyR)
#rR = PWM(ledrR)
#gL = PWM(ledgL)
#yL = PWM(ledyL)
#rL = PWM(ledrL)


def setThings():
    while True:
        hz = input("Enter a frequenzy from 0 - 20\n")
        power = input("Enter how bright you want the light to be from 0% to 100%\n")
        if hz.isdigit():
            if power.isdigit():
                break
            else:
                setThings()
        else:
            setThings()
    if int(hz) == 0:
        print("Invalid input not in range")
        setThings()
    elif int(hz) > 20:
        print("Invalid input too high")
        setThings()
    elif int(power) < 0:
        print("Invalid input too low")
        setThings()
    elif int(power) > 100:
        print("Invalid input too high")
        setThings() 
    elif not hz.isdigit():
        setThings()
    elif not power.isdigit():
        setThings()
    
    sleeptimer = 1000 / int(hz)
    duty = int(power) / 100 * 65535 
    
    print(int(duty))
    print(sleeptimer) 
    gR.freq(800)
    while True:
        gR.duty_u16(int(duty))
        sleep_ms(int(sleeptimer))
        gR.duty_u16(1)
        sleep_ms(int(sleeptimer))

while True:
    setThings()
#while True:
#    gR.freq(800)
#    gL.freq(800)
#    gL.duty_u16(0)
#    gR.duty_u16(2**16)
#    sleep_ms(500)
#    gR.duty_u16(0)
#    gL.duty_u16(2**16)
#    sleep_ms(500)


