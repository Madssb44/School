#########################################################################################
# IMPORTS 
#########################################################################################
import time
from machine import Pin


#########################################################################################
# SETTING PINS 
#########################################################################################
gy53 = Pin(14, Pin.IN)


#########################################################################################
# LOCAL VARIABLES 
#########################################################################################
distance = []      # CM 
pwm_rising = 0     # Starting time for measurement calc
pwm_pulse = 0      # Ending time for measurement calc 


#########################################################################################
# INIT FOR IRQ 
#########################################################################################
def gy53_irq_init():
    """Sets up the interrput for the gy53"""
    gy53.irq(trigger= Pin.IRQ_RISING | Pin.IRQ_FALLING, handler= tof_irq_handler )

#########################################################################################
# IRQ HANDLER 
#########################################################################################
def tof_irq_handler( gy53 ):
    """interrput handler for GY-53 sensor
    if sensor is starting a measurement the starting time is saved
    then the sensor is done the ending time is used to calculate the distance in cm

    Param: Pin
    Return: appends distance to list of measurements
    Warning: Pin must be set and have irq enabled"""
    global pwm_pulse, pwm_rising
    if gy53.value() == 1:
        pwm_rising = time.ticks_ms()
    else:
        pwm_pulse = time.ticks_ms()
        dist_cm = (pwm_rising - pwm_pulse) / 100 
        distance.append(dist_cm)

########################################################################################
# PUBLIC FUNCTIONS
########################################################################################
def get_distance()-> float:
    """Takes the last 3 measurements and finds the median 
    for the most accurate measurement

    Param: None
    Return: distance in cm
    Warning: Will delete old measurements when done"""
    distance_temp = distance[-1,-2,-3]
    distance_temp.sort()
    distance = distance_temp 
    cm = distance_temp[1]
    return cm 


