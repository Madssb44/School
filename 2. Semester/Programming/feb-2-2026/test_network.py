from network import WLAN
import socket
import webrepl 
from machine import Pin, idle

board_led = Pin("LED", Pin.OUT
wlan = WLAN(WLAN.IF_STA) 

wlan.active(True)

wlan.config(hostname="MB TEST")

wlan.connect("ITEK 1st","itekf25v")

webrepl.start(password="aoeu")
HOST = "0.0.0.0"
PORT = 50000

try:
    while True: 
        print(f"recieving from {addr}: {data}") 
        data = data.decode('ascii').strip('\n').lower()
        if data == "toggle":
            led.toggle()
        elif data == 'on':
            led.on()
        elif data == 'off':
            led.off()

