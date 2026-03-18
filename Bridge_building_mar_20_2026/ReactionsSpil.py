############################################
# Reaktionsspil GRUPPE 6
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
WIFI_SSID = '##########'                      
WIFI_PASS = '##########'
ACCESS_TOKEN = '##########'
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
    time.sleep_ms(random.randrange(2000,8000,1))
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
    print(f"Din tid er: {resultat}ms")
    time.sleep(1)
    if resultat < 80:
        print("Det var lidt for hurtigt til at være en reaction så lad os springe den over på scoreboardet")
        time.sleep(2)
    else:
        navn = input("Skriv dit navn her: ")
        send_data(resultat, navn)


############################################
# SEND DATA 
# 
# Sender resultatet til thingsboard så det kan blive displayet på dashboardet
############################################
def send_data(resultat, navn):
    client.connect()
    telemetry = {"match tid": resultat, "match navn": navn}
    client.send_telemetry(telemetry)
    client.disconnect()


#############################################
# EKSTRA OPGAVE
#
# Tids match spil 
# 
# Det er muligt at lave et spil mere med det allerede bygget spil 
# Her under er der noget kode der kræver lidt mere redigering
# Det består af 4 dele
# - tid_at_matche er en function der skal får lyset til at tende i en tilfældigt mengde tid 
# - spiller_tid er en function der skal aflæse hvor lang tid spilleren holder knappen nede i 
# - calc_diff er en function der skal udregne foreskellen spillerens tid og den tilfældige tid 
# - send_match_data er en function der skal sende informationen til dashboardet
#############################################


#############################################
# TID AT MATCHE 
#
# denne function setter en tilfældig timer 
# og får knappen til at lyse i den tilfældige tid. 
#############################################

def tid_at_matche():
    time.sleep(2)
    tid = random.randrange(1000,8000,1)
    led.on()
    time.sleep_ms(tid)
    led.off()
    print("Vær klar til at matche om")
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    spiller_tid(tid)


#############################################
# SPILLER TID 
#
# Denne function ender knappen og venter på at den bliver trykket på
# Mens den bliver holdt inde teller en timer op indtil at der blive givet slip på knappen 
#############################################

def spiller_tid(tid):
    led.on()

    while switch.value() == 0:
        time.sleep(0.01)

    while switch.value() == 1:
        time.sleep(0.01)
    start = time.ticks_ms()

    while switch.value() == 0:
        time.sleep(0.01)
    end = time.ticks_ms()
    led.off()
    calc_diff(start, end, tid)


#############################################
# CALC DIFF 
#
# Denne function udregner foreskellen mellem de 2 tider men hvordan gør man nu det??? 
# 
# foo, bar & foobar skal erstattes af de rigtige variabler (start, end, tid)
# og udregningen skal laves så functionen kan beregne det rigtige resultatet
#############################################
def calc_diff(start, end, tid):
    resultat = foo +-*/() bar +-*/() foobar 
    print(f"Dit resultat er: {resultat}ms")
    time.sleep(1)
    navn = input("Skriv dit navn her: ")
    send_match_data(resultat, navn)


#############################################
# SEND MATCH DATA
#
# Denne function sender navn og resultatet til dashboardet, men hvordan er det nu jeg modtager det? 
#
# Hvilke parameter skal functionen burge?
# Hvad skal sendes som navn og hvad skal sendes som tid?
#############################################
def send_match_data(???, ???): 
    client.connect()
    telemetry = {"match tid" : ???, "match navn" : ???}
    client.send.telemetry(telemetry)
    client.disconnect()


#############################################
# Hvad så nu?
#
# Hvad skal så gøres for at starte spillet?
#############################################


#############################################
# Det her er for nemt opgaverne 
#
# Ville man kunne lave en mulighed at vælge spil på?
# Fra terminalet, med knappen? 
#
# Er der flere spil/ting man ville kunne lave? 
# memory game, morsekode oversætter, tryk på 10 sec?
#############################################



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
