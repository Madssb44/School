import random

v_base_speed = 80 # % of max speed 
r_base_speed = 80 # % of max speed 

target_dist = 30 # CM


P_value = 0.33
I_value = 0.02

dist = measure()
if dist > 120: # sets dist to 120 if measurement is higher than 120
    dist = 120

error = target_dist - dist # calculates the error 

P = error * P_value # finds P's value 

# finds I and or makes I if no I was already made
if I:
    I = error + I / 2
else:
    I = error

reg = P * I 



