#####################################################
# Importing modules
#####################################################
import time
from machine import Pin



#####################################################
# SETTING PINS 
#####################################################
ref_sens = Pin(15, Pin.IN)  # Initialize pin


#####################################################
# LOCAL VARIABLES 
#####################################################
box = False  


#####################################################
# INIT FOR IRQ  
#####################################################
def ref_irq_init():
    """Init function for ir sensors irq

    Param: None
    Return: None
    Warning: Must be called for interrupts to work"""
    ref_sens.irq(trigger = Pin.IRQ_RISING, handler = ref_irq_handler)


######################################################
# IRQ HANDLER  
######################################################
def ref_irq_handler( ref_sens ):
    """Handler for ir sensor
    Will make the car drive forwards when going out of bounds

    Param: Pin 
    Return: None 
    Warning: ref_irq_init must be called first"""
    global box
    RC_car.move_forward(60)
    box = False 


######################################################
# PUBLIC FUNCTIONS 
######################################################
def check_box():
    """Checks if box is found or not

    Param: None 
    Return: bool
    Warning: Will effect movement in sumo mode"""
    global box
    return box 

def found_box():
    """sets box to true when a box is found

    Param: None
    Return: None
    Warning: Will effect movement in sumo mode"""
    global box
    box = True 
    




