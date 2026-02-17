# Start of tof task 
from machine import Pin 
from time import ticks_us 

#############################################################
# Module setup
#############################################################

#############################################################
# Hardware config
#############################################################
led = Pin( "LED", )
pwmPin = Pin( 14, Pin.IN )

#############################################################
# Local variables
#############################################################
PWM_RISING = 0
distance_mm = 0
PWM_count = 0

#############################################################
# Name definitions
#############################################################

###################################################################################################
# Public functions
###################################################################################################

###################################################################################################
# Brief         PWM ISR function. Called everytime PWM is rising 
#
# Param[in]     None
# Return        None
#
# Warning       Called from IRQ
###################################################################################################

###################################################################################################
# Brief         Init function
#
# Param[in]     None
# Return        None
#
# Warning       Must be called at power up
###################################################################################################
def C_TOF_TASK_Init():
    # Init for the car with a IRQ on the PWM Pin 
    pwmPin.irq( handler = pwm_IRQ_handler_ISR, trigger = Pin.IRQ_RISING | Pin.IRQ_FALLING)
    print("Robocar initilazed")

###################################################################################################
# Brief         Measures and calculates with the TOF sensor
#
# Param[in]     
# Return        None
#
# Warning       None
###################################################################################################
def pwm_IRQ_handler_ISR( irqPin ):
    global PWM_RISING, distance_mm, PWM_count
    
    if irqPin.value() == 1:
        PWM_RISING = ticks_us()

    else:
        PWM_width_us = time.ticks_us() - PWM_RISING
        # The datasheet form the GY-53 says to find the distance in mm you need to calc = time in us / 10  
        if PWM_width_us > 20000:
            distance_mm = 2000 
        else:
            distance_mm = PWM_width_us / 10
    PWM_count =+ 1
        

###################################################################################################
# Brief         sends the measurements to the caller
#
# Param[in]     None
# Return        int|float
#
# Warning       Must be called at power up
###################################################################################################
def C_robocar_get_distance():
    global distance_mm 
    print(f"sending distance = {distance_mm}mm")
    return distance_mm 


###################################################################################################
# Brief         task function passes for now
#
# Param[in]     None
# Return        None
#
# Warning       Must be called at power up
###################################################################################################
def C_robocar_check_pwm():
    global PWM_count

    if PWM_count < 10:
        distance_mm = 0 
    PWM_count = 0





