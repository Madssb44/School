from ..main import RC_car
from sensors import *
import time

i_sum = 0.0 


def pi_calc(cm):
    global i_sum
    base_speed = 50000
    base_turning = 35000
    p_val = 1500 
    i_val = 0.1
    target_dist = 30

    error = target_dist - cm    
    p = error * p_val 
    i_sum = i_sum + i_val * error 

    duty = p * i_sum
    if not 10 < error > -10:
        if error > 0:
            error = 10
        else:
            error = -10
    
    if error > 0:
        r_duty = int( duty + base_turning )
        l_duty = int( duty + base_speed ) 
    else:
        r_duty = int( duty + base_speed )
        l_duty = int( duty + base_turning )

    return r_duty, l_duty
    
    
def wall_main():    
    r_duty, l_duty = pi_calc(get_distance)
    RC_car.custome(1, 0, 1, 0, r_duty, l_duty )

