# /udp_main.py
from movement import motor
from network import WLAN
from modes import Sumo, Wall
from sensors import hall_sens
import machine
import socket
import time

wall = False

sumo = False

lm = None 
def UDP_Listen():
    
    global wall, sumo, lm 
    # Setup socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet protocol, UDP
    soc.bind(("0.0.0.0", 12345)) # Bind the socket to the machines own IP, and port 12345 
    
    # Indicate program is ready
    speed = 60
    start = time.ticks_ms()
    try:
        while True:
            # Wait for a command

            
            check = time.ticks_ms()
            out = check - start 
            if out > 1000:
                print("\n\n\n\n\n\n\n\n\n\n",round(hall_sens.calc_speed(),1), "mps")
                start = time.ticks_ms()
                
            data, addr = soc.recvfrom(1024)
            
            # Convert data from bytes to string
            data = data.decode('ascii').strip('\n').lower()
                                        
            #print("Received from", addr, ":", data)
            
            # Handles speed cases with edge case control movement recall 
            if data == '1':
                speed = 100
                if lm:
                    data = lm
                    lm = None
                    
            if data == '2':
                speed = 80
                if lm:
                    data = lm
                    lm = None
            if data == "3":
                speed = 60
                if lm:
                    data = lm
                    lm = None


            # Handle command
            if data == 'w':
                motor.move_forward(speed)
                lm = data
                
            elif data == 's':
                motor.move_back(speed)
                lm = data
                
            elif data == 'd':
                motor.q_turn_right(speed)
                lm = data
                
            elif data == 'a':
                motor.q_turn_left(speed)
                lm = data
                
            elif data == 'wd':
                motor.turn_right(speed)
                lm = data
                
            elif data == 'wa':
                motor.turn_left(speed)
                lm = data
                
            elif data == "stop":
                motor.stop_motors()
                lm = data 
                
            #elif data == '2':
            #    sumo = True
            #    Sumo.find_box()
            #elif data == '1':
            #    wall = True
            #    Wall.find_wall()
            #elif data == '3':
            #    motor.stop_motors()
            #elif data == '5':
            #    Sumo.dummy()

            #else:
            #    if wall == True:
            #        if data == "4":
            #            wall = False
            #            motor.stop_motors()
            #        else:
            #            Wall.find_wall()
            #    if sumo == True:
            #        if data == "4":
            #            sumo = False
            #            motor.stop_motors()
            #        else:
            #           Sumo.find_box()

    except Exception as e:
        # If the program is interrupted, we need to close the port
        soc.close()
        raise e # Re-raise the error, so the program exits properly
