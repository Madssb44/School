# målinger
import time
from machine import Pin


gy53 = Pin(14, Pin.IN)  # Initialize GY-53 I2C pin

distance = [] # CM 
pwm_rising = 0 
pwm_pulse = 0 
def gy53_irq_init():
    gy53.irq(trigger= Pin.IRQ_RISING | Pin.IRQ_FALLING, handler= tof_irq_handler )


def tof_irq_handler( gy53 ):
    global pwm_pulse, pwm_rising
    """measures the distance with the GY-53 sensor and returns the measurement in CM"""
    if gy53.value() == 1:
        pwm_rising = time.ticks_ms()
    else:
        pwm_pulse = time.ticks_ms()
        dist_cm = (pwm_rising - pwm_pulse) / 100 
        distance.append(dist_cm)

def get_distance()-> float:
    distance_temp = distance[-1,-2,-3]
    distance_temp.sort()
    distance = distance_temp 
    cm = distance_temp[1]
    return cm 


