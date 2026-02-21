#Importing modules
import time
from machine import Pin
from movement import motor

# setting the pin for the Reflection sensor 
ref_sens = Pin(15, Pin.IN)  # Initialize pin


#####################################################
# Init for ref sensor 
#####################################################
def ref_irq_init():
    ref_sens.irq(trigger = Pin.IRQ_FALLING, handler = ref_irq_handler)


######################################################
# ref sensor handler 
######################################################
def ref_irq_handler( ref_sens ):

    turning = True 
    start = time.ticks_ms()

    motor.q_turn_right(50)
    while turning:
        now = time.ticks_ms()
        if (now - start) <= 300:
            turning = False

    motor.move_forward(40)



  




