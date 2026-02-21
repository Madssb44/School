from ..main import RC_car
from sensors import *
import time

i_sum = 0.0 


def pi_calc(cm):
    global i_sum
    p_val = 5000
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
        r_duty = int(duty * 0.8)
        l_duty = duty 
    else:
        r_duty = duty
        l_duty = int(duty * 0.8)
    
    return r_duty, l_duty
    
    
def wall_main():    
    r_duty, l_duty = pi_calc(get_distance)
    RC_car.custome(1, 0, 1, 0, r_duty, l_duty )

