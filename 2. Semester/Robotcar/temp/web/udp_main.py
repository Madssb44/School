# /main.py
from movement import motor
from network import WLAN
from modes import Sumo, Wall
import socket
sumo = False
wall = False 

def UDP_Listen():
    global sumo, wall 
    # Setup socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet protocol, UDP
    soc.bind(("0.0.0.0", 12345)) # Bind the socket to the machines own IP, and port 12345

    try:
        while True:
            # Wait for a command
            data, addr = soc.recvfrom(1024)

            # Convert data from bytes to string
            data = data.decode('ascii').strip('\n').lower()

            print("Received from", addr, ":", data)



            # Handle command
            if data == 'w':
                motor.move_forward(80)
            elif data == 's':
                motor.move_back(80)
            elif data == 'd':
                motor.q_turn_right(80)
            elif data == 'a':
                motor.q_turn_left(80)
            elif data == 'wd':
                motor.turn_right(80)
            elif data == 'wa':
                motor.turn_left(80)
            elif data == '2':
                Sumo.find_box()
                sumo = True 
            elif data == '1':
                Wall.find_wall()
                wall = True 
            elif data == '3':
                motor.stop_motors()

            else:
                print(30*"\n")
                if wall == True:
                    if data == "3":
                        motor.stop_motors()
                        wall = False 
                    else:
                        Wall.find_wall()

                elif sumo == True:
                    if data == "3":
                        motor.stop_motors()
                        sumo = False 
                    else:
                        Sumo.find_box()
                else:
                    motor.stop_motors()
                    print("Waiting for data")


    except Exception as e:
        # If the program is interrupted, we need to close the port
        soc.close()
        raise e # Re-raise the error, so the program exits properly
