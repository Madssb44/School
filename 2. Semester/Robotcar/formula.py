import math
import random


def find_speed(speed: int) -> int:
    """calculates the pwm from the given speed in procent from 0-100 as an int
    param:speed
    return:int
    """
    # finds the working range for the motor
    pwm_range = 2**16 - 15000
    # finds the value of 1% from the range
    pwm_in_procent = pwm_range / 100
    # Uses the speed param given to find the duty the pwm module needs to get the motor to drive at that %
    duty = speed * pwm_in_procent
    return int(duty)


def steering_from_error(d_target=30, e_max=10) -> int:
    """Finds out how much to set each wheels steer to so it can adjust to the wall
    param:distance_target in cm, e_max the max error reading
    return:int"""

    # Finds the error distance from a random int
    error = d_target - random.randint(0, 100)
    print(error)
    e_norm = max(100, min(0, error / e_max))
    # Finds the steer from the e_norm set before
    steer = math.sin((math.pi / 2) * e_norm)

    return int(steer)


def control(base_speed=find_speed(70), steer_gain=find_speed(30)):
    steer = steering_from_error()
    print(steer)

    left = base_speed + steer_gain * steer
    right = base_speed - steer_gain * steer
    print(left)
    print(right)

    left = max(250, min(0, left))
    right = max(-250, min(0, right))

    return left, right


# Sets right and left motor to 0 in 16 bit pwm range
right_motor = 0
left_motor = 0


# Target distance in cm
d_target = 30

# Sets max error distance
e_max = 10

base_speed = find_speed(70)
steer_gain = find_speed(30)


for i in range(100):
    left, right = control()
    print(f"speed set for left = {left} \nspeed set for right = {right}")




"""

target_dist = 40 # target to drive at 
dist = meanure() # func for measuring the current dist 
error = dist - target_dist # find the error 

e_max = 50
e_min = -20 



def calc_duty(error, side):
    

def find_steer(tgd,dist,error,side):
    if side ==  r and error > 10:
        duty = calc_duty()
    elif side == l and error > 10:
        duty = calc_duty()
    elif side == r and error > -10:
        duty = calc_duty()
    elif side == l and error > -10:
        duty = calc_duty()
            return duty


if error < -10: 
    get further
    
    right wheel low
    left wheel high 

if error > 10: 
    get closer 

    right wheel high
    left wheel low 

else:
    go forward


"""
