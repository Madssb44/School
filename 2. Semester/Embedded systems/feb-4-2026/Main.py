from sys import activate_stack_trampoline
from time import sleep


###################################################################################################
# Globale variabler for dette modul
###################################################################################################
SM_TICK_MS = 100 # Vores tilstandsmaskine kører i et loop med 100 ms interval
iTimer_ms = 0 # Bruges som stopur til at generere et TIMEOUT event

###################################################################################################
# STATE
###################################################################################################
STATE_INIT = 0
STATE_STOP = 1 
STATE_STOP_ACCEPT_BUTTON = 2
STATE_WALK = 3

###################################################################################################
# EVENT
###################################################################################################
EVENT_INIT_OK = True 
EVENT_BUTTON_PRESS = False
EVENT_TIMEOUT = False 


###################################################################################################
# ACTION
ped_signal_walk_desc = "Red off, Green on, timer -> 10sec"
ped_signal_stop_desc = "Red on, Green off, timer -> 10sec"
active_indicator_light_on_desc = "indicator light on"
active_indicator_light_off_desc = "indicator light off"
set_timer_func = "sets timer" 


###################################################################################################

###################################################################################################
# @brief        Action A for the statemachine
#               Prints a dummy string in Terminal
#
# @param[in]    None
# @param[out]   None
# @return       None
#
# @warning      None
###################################################################################################
def ped_signal_stop():
    print(ped_signal_stop_desc)
    # TODO Insert your action code here


###################################################################################################
# @brief        Action B for the statemachine
#               Prints a dummy string in Terminal
#
# @param[in]    None
# @param[out]   None
# @return       None
#
# @warning      None
###################################################################################################
def ped_signal_walk():
    print(ped_signal_walk_desc)
    # TODO Insert your action code here


###################################################################################################
# @brief        Action B for the statemachine
#               Prints a dummy string in Terminal
#
# @param[in]    None
# @param[out]   None
# @return       None
#
# @warning      None
###################################################################################################
def active_indicator_light_on():
    print(active_indicator_light_on_desc)
    # TODO Insert your action code here


###################################################################################################
# @brief        Action B for the statemachine
#               Prints a dummy string in Terminal
#
# @param[in]    None
# @param[out]   None
# @return       None
#
# @warning      None
###################################################################################################
def ped_signal_stop():
    print(ped_signal_stop_desc)
    # TODO Insert your action code here


###################################################################################################
# @brief        Action B for the statemachine
#               Prints a dummy string in Terminal
#
# @param[in]    None
# @param[out]   None
# @return       None
#
# @warning      None
###################################################################################################
def active_indicator_light_off():
    print(active_indicator_light_off_desc)
    # TODO Insert your action code here


###################################################################################################
# @brief        Sets the timer seconds. When timer runs out, EVENT_TIMER is thrown
#
# @param[in]    None
# @param[out]   None
# @return       None
#
# @warning      None
###################################################################################################
def set_timer( iTimerValue_sec ):
    global iTimer_ms
    iTimer_ms = iTimerValue_sec 


###################################################################################################
# EVENT tjek
###################################################################################################

###################################################################################################
# TODO: Lav en funktion der tæller iTimerValue_sec ned. Når den bliver 0, skal event sættes til True
# Funktionen skal kaldes fra main loop med 100 ms interval
###################################################################################################
def checkEventTimer():
    # TODO


###################################################################################################
# Initier programmet (startup), inden vi starter selve programmet
###################################################################################################
# Start med at sætte aktiv state til den vi skal starte med efter startup:
smActiveState = STATE_A
smAction_A()
smSetTimer( 1000 )


###################################################################################################
# Tilstandsmaskine task (100 ms)
###################################################################################################
while True:

    ###############################################################
    # STATE_A
    ###############################################################
    if smActiveState == STATE_INIT:
        if EVENT_INIT_OK == True:
            # ACTION:
            ped_signal_stop()
            active_indicator_light_off()
            # TRANSITION:
            smActiveState == STATE_STOP 

    ###############################################################
    # STATE_B
    ###############################################################
    elif smActiveState == STATE_STOP: 

        if EVENT_B == True:
            # ACTION: Insert your action code here:
            # TODO...
            # TRANSITION: Set the new STATE here, if you want t change state now:
            # TODO... 
            # Reset event:
            # TODO...
    elif smActiveState == STATE_STOP_ACCEPT_BUTTON:

    elif smActiveState == STATE_WALK:
        
    # Tjek for events:
    # TODO: Kald denne funktion for at tjekke for TIMEOUT EVENT : checkEventTimer()

    # Kør tilstandsmaskinen i et loop på 10 gange i sekundet (100 ms interval):
    sleep( SM_TICK_MS/1000 )
