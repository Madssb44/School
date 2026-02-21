############################################################
# IMPORTS 
############################################################
from ..main import RC_car
from sensors import TOF, REF_sens
import time


###########################################################
# LOCAL VARIABLS
###########################################################
push_time = 0 # ms 
turning = False # Becomes true while turning to face the box 
turn_time = 1000 # ms 
reset = False # becomes true when it finds a box 


###########################################################
# LOGIC FOR SUMO MODE 
###########################################################
def sumo_main():
    """Main logic loop for sumo mode

    Param: turning, reset 
    Return: can set reset & turning to true if criteria is meet 
    Warning: Needs to have ref & tof sensor interrupts to be enabled """
    global turning, reset
    box = REF_sens.check_box()
    
    if reset:
        if box:
            if turning:
                setting_up()
            else:
                push()
        else:
            go_back()
    elif not box:
        cm = TOF.get_distance()
        if 70 < cm > 10:
            REF_sens.found_box()
            reset = True
            turning = True
            RC_car.stop()
        else:
            find_box()
        
###########################################################
# MOVEMENT FUNCTIONS
###########################################################
def find_box():
    """Custome movement for finding a box

    Param: None 
    Return: None 
    Warning: Make sure you know your pins! """
    RC_car.custom_movement(1,0,1,0,30,80)


def go_back():
    """resets position after box has been pushed out 

    Param: reset, push_time 
    Return: lowers push time and sets reset to false when pushtime is at 0 
    Warning: None """
    global push_time, reset 
    if push_time:
        RC_car.move_forward(50)
        push_time -= 10
    else:
        reset = False 


def push():
    """pushes the box and counts each time its called

    Param: push_time
    Return: Raises push timer 
    Warning: None"""
    global push_time 
    RC_car.move_back(50)
    push_time += 10  


def setting_up():
    """Sets the car up to push the box

    Param: turning, turn_time
    Return: lowers turn timer until its done turnig then it resets turning and the timer 
    Warning: None """
    global turning, turn_time 
    if turn_time:
        RC_car.q_turn_right(50)
        turn_time -= 10
    else:
        turn_time = 1000 
        turning = False 

