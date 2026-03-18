############################################
# Reaktionsspil GRUPPE 4
############################################


############################################
# IMPORTS
############################################
from machine import Pin
import time
import random
import network
from thingsboard_sdk.tb_device_mqtt import TBDeviceMqttClient


############################################
# HARDWARE SETUP
############################################
led = Pin(2, Pin.OUT)
switch = Pin(1, Pin.OUT, Pin.PULL_DOWN)
THINGSBOARD_HOST = "eu.thingsboard.cloud"


############################################
# FUNKTIONER
############################################

############################################
# WIFI SETUP
#
# Under konfig sektionen kan du indtaste WiFi-oplysninger og Thingsboard token.
# 
# I skal indsætte navn, password og token.
############################################

# ----------- KONFIG -----------
WIFI_SSID = 'ITEK 2nd'                      
WIFI_PASS = '2nd_Semester_F25v'
ACCESS_TOKEN = 'pLE85M213gBjTKsdiPcn'
client = TBDeviceMqttClient(THINGSBOARD_HOST,1883, ACCESS_TOKEN)

# ----------- WIFI ----------- 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASS)

# ----------- VENT PÅ FORBINDELSE -----------
print("Forbinder til WiFi...")
while not wlan.isconnected():
    time.sleep(0.5)
print("WiFi forbundet:", wlan.ifconfig())


############################################
# START SPIL
#
# Venter på at knappen bliver trykket to gange hurtigt for at starte spillet.
############################################
def start_game(count):
    switch.on()
    count = 0
    while True:
        if switch.value() == 0:
            count += 1
            time.sleep(0.2)
        if count >= 2:
            react_game()
            break


############################################
# SPIL LOGIK
# 
# Starter tilfældig timer mellem 1-5 sekunder.
# Når timeren er slut, bliver LED-knappen tændt.
# Når lyset er tændt og der trykkes på knappen bliver tiden taget og bliver sendt videre til "calc_result".
############################################
def react_game():
    time.sleep(random.randrange(1,5,1))
    start_time = time.ticks_ms()

    led.on()
    switch.on()
    while True:
        if switch.value() == 0:
            end_time = time.ticks_ms()
            led.off()
            time.sleep(0.2)
            calc_result(start_time,end_time)
            break


############################################
# UDREGNING AF RESULTAT
#
# Udregner resultatet i ms og sender data til Thingsboard.
############################################
def calc_result(start, end):
    resultat = end - start
    navn = input("Skriv navn her: ")
    send_data(resultat, navn)

def send_data(resultat, navn):
    client.connect()
    # Send the raw integer instead of a string
    telemetry = {"match tid": resultat, "match navn": navn}
    client.send_telemetry(telemetry)
    client.disconnect()

    
############################################
# MAIN LOOP
############################################
def main():
    print("###########################################")
    print("Tryk på knappen to gange hurtigt")
    print("###########################################")
    while True:
        start_game(0)
        break


############################################
# START PROGRAM
############################################
while True:   
    main()