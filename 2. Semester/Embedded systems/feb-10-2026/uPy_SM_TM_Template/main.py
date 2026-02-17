from machine import Timer

#############################################################
# Import external modules
#############################################################
from C_LED import *
from C_SM_Main import *
from C_TM import *
from robocar import *
from tof_task import *

#############################################################
# Module setup
#############################################################

#############################################################
# Hardware config
#############################################################
# 1 ms timer interrupt:
# Define the IRQ callback ISR:
def tick(timer):
    C_TM_Update_ISR()
# Setup timer interrupt:
# It is necessary to ignore a warning, because the interpreter 
# expects an argument for the Timer() function.
tim = Timer() # type: ignore
tim.init(freq=1000, mode=Timer.PERIODIC, callback=tick)

#############################################################
# Local variables
#############################################################


#############################################################
# Init external modules
#############################################################
C_LED_Init()
C_TM_Init()
C_SM_Main_Init()
C_robocar_Init()

#############################################################
# Start tasks
#############################################################
C_TM_CreateTask( "LED", 10, C_LED_Task )
C_TM_CreateTask( "SM_MAIN", 100, C_SM_Main_task)
C_TM_CreateTask( "CHECK_PWM", 100, C_robocar_check_pwm)
# Add more tasks here...

###################################################################################################
# Application is now ready to fly...
###################################################################################################
print("Application running...")

# Test LED: Make it FLASH:
# Remove if you don't need it.
#C_LED_SET_MODE( LEDName.LED_PICO, LEDMode.LED_MODE_BLINK, 1000 )

# Main loop: Simply calls the TM as fast as possible
# TM is now in control of the system.
while True:
    C_TM_Execute()


