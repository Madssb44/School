#########################################################
# Import external modules
#########################################################
from machine import Timer
from sensors import TOF, hall_sens, REF_sens
from movement import motor 
from web import udp_main
import TM


#########################################################
# Hardware config
#########################################################
# 1 ms timer interrupt:
# Define the IRQ callback ISR:
def tick( timer ):
    tm_update_isr()

tim = Timer()
tim.init(freq=1000, mode=Timer.PERIODIC, callback=tick)


#########################################################
# internal init modules
#########################################################
udp_main.UDP_init()
hall_sens.hall_irq_init()
REF_sens.ref_irq_init()
TOF.tof_irq_init()
RC_car = motor.Car(16,17,18,19,20,21, l_offset=4)


#########################################################
# CREATS TASKS
#########################################################
TM.create_task( UDP_LISTENER, 10, UDP_listen )
TM.create_task( CALC_SPEED, 1000, calc_speed )
TM.create_task( PRINT_TO_TERMINAL, 1000, print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGoing at {hall_sens.get_speed()} cmps"))


#########################################################
# EXECUTES TASKS
#########################################################
while True:
    TM.tm_execute_task()
