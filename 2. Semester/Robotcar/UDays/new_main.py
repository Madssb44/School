from machine import Timer

from TM import tm_execute_task, tm_update_isr
#########################################################
# Import external modules
#########################################################
from sensors import *
from movement import *
from web import *
from modes import *
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
hall_irq_init()
ref_irq_init()
tof_irq_init()


#########################################################
#
#########################################################
create_task( UDP_LISTENER, 10, IDP_listen )
create_task( CALC_SPEED, 1000, calc_speed )
create_task( PRINT_TO_TERMINAL, 300, print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGoing at {get_speed} cmps"))

#########################################################
#
#########################################################

#########################################################
#
#########################################################
while True:
    tm_execute_task()
