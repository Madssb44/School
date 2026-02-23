# /udp_main.py
from modes import *
from sensors import *
from ..main import RC_car
import socket

wall = False 
sumo = False
lm = None 

speed = 80



soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



def UDP_init():
    global soc
    soc.bind(("0.0.0.0", 12345))

def UDP_listen():
    global soc, wall, sumo, lm, speed 
    try:
        # Wait for a command
        data, addr = soc.recvfrom(1024)
            
        # Convert data from bytes to string
        data = data.decode('ascii').strip('\n').lower()


            # Handle command
        if data == 'w':
            RC_car.move_forward(speed)
                
        elif data == 's':
            RC_car.move_back(speed)
                
        elif data == 'd':
            RC_car.q_turn_right(speed)
                
        elif data == 'a':
            RC_car.q_turn_left(speed)
                
        elif data == 'e':
            RC_car.turn_right(speed)
                
        elif data == 'q':
            RC_car.turn_left(speed)
                
        elif data == "stop":
            RC_car.stop_motors() 
                
        elif data == '2':
            sumo = True
            sumo_main()
        
        elif data == '1':
            wall = True
            wall_main()
        
        elif data == '3':
            RC_car.stop()
        
        else:
            if wall == True:
                if data == "4":
                    wall = False
                    RC_car.stop()
                else:
                    wall_main()
            if sumo == True:
                if data == "4":
                    sumo = False
                    RC_car.stop()
                else:
                   sumo_main()
            else:
                if data == "nothing":
                    if speed < 30:
                        RC_car.stop()
                    else:
                        speed -= 2

                    

    except Exception as e:
        # If the program is interrupted, we need to close the port
        soc.close()
        raise e # Re-raise the error, so the program exits properly

