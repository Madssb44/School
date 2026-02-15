from C_LED import C_LED_SET_MODE, LEDName, LEDMode
from robocar import * 
from tof_task import * 

#############################################################
# Module setup
#############################################################
SM_TICK_MS = 100

#############################################################
# Name definitions used by the Statemachine
#############################################################
# SM STATES:
STATE_CLOSE                  = 0
STATE_FAR                    = 1

# SM EVENTS:
EVENT_TIMEOUT = False
EVENT_DISTANCE_CLOSE = False
EVENT_DISTANCE_FAR = False 

#############################################################
# Local variables
#############################################################
iTimer_ms = 0 # Bruges som stopur til at generere et TIMEOUT event
smActiveState = STATE_CLOSE 

#############################################################
# Private functions
#############################################################

##############################################################
# ACTION functions
# the next functions are the ACTIONS used by the Statemachine
##############################################################

###################################################################################################
# Brief         Action A for the statemachine
#
# Param[in]     None
# Return        None
#
# Warning       None
###################################################################################################
def smAction_CLOSE():
    global distance_mm 
    # Example code. Insert your own ACTIOn code
    C_LED_SET_MODE( LEDName.LED_PICO, LEDMode.LED_MODE_ON, 500 )
    print(30 * "\n")
    print(f"Current active state: FAR \nCurrent distance measured: {distance_mm}")

###################################################################################################
# Brief         Action B for the statemachine
#
# Param[in]     None
# Return        None
#
# Warning       None
###################################################################################################
def smAction_FAR():
    global distance_mm 
    # Example code. Insert your own ACTIOn code
    C_LED_SET_MODE( LEDName.LED_PICO, LEDMode.LED_MODE_FLASH, 500 )
    print(30 * "\n")
    print(f"Current active state: CLOSE\nCurrent distance measured: {distance_mm}")

###################################################################################################
# Brief         Sets the timer in seconds.
#
# Param[in]     None
# Return        None
#
# Warning       None
###################################################################################################
def smSetTimeout_sec( iTimerValue_sec ):
    global iTimer_ms
    iTimer_ms = iTimerValue_sec * 1000


##############################################################
# EVENT functions
# the next functions checks if an EVENT must be set
##############################################################

###################################################################################################
# Brief         Check if the Timer has run out. Set EVENT_TIMER when timer is 0.
#
# Param[in]     None
# Return        None
#
# Warning       Must be called every time the Statemachine is called
###################################################################################################
def checkEVENT_TIMEOUT():
    global iTimer_ms
    global EVENT_TIMEOUT

    if iTimer_ms > 0:
        iTimer_ms -= SM_TICK_MS
        # Aktiver TIMEOUT event hvis vi når nul:
        if iTimer_ms <= 0:
            EVENT_TIMEOUT = True

###################################################################################################
# Brief         Check if distance detects CLOSE or FAR 
#
# Param[in]     None
# Return        None
#
# Warning       None
###################################################################################################
def check_EVENT_DISTANCE():
    global EVENT_DISTANCE_CLOSE, EVENT_DISTANCE_FAR, EVENT_TIMEOUT

    # In state CLOSE we check if the car is too close to the wall
    if smActiveState == STATE_CLOSE:
        if C_robocar_get_distance() > 300:
            EVENT_DISTANCE_FAR = True  
            EVENT_DISTANCE_CLOSE = False  

    elif smActiveState == STATE_FAR:
        if C_robocar_get_distance() < 200:
            EVENT_DISTANCE_CLOSE = True   
            EVENT_DISTANCE_FAR = False 
    
    smSetTimeout_sec( 1 )
#############################################################
# Public functions
#############################################################
###################################################################################################
# Brief         Initialize Statemachine before it is started
#
# param[in]     None
# Return        None
#
# Warning       Must be called at system startup before C_SM_Main_task is started
###################################################################################################
def C_SM_Main_Init():
    global smActiveState

    # Start med at sætte aktiv state til den vi skal starte med efter startup:
    # Hvad der skal ske her afhænger af jeres program.
    # Det er forskelligt hvad der skal til for at "kickstarte" dit program
    smActiveState = STATE_CLOSE
    smAction_CLOSE()
    smSetTimeout_sec( 1 )

###################################################################################################
# Brief         This task controlles the main Statemachine in the system
#
# param[in]     None
# Return        None
#
# Warning       Must be called with SM_TICK_MS interval
###################################################################################################
def C_SM_Main_task():
    global smActiveState   
    global EVENT_TIMEOUT
    global EVENT_DISTANCE_FAR
    global EVENT_DISTANCE_CLOSE
    

    if EVENT_TIMEOUT == True:
###############################################################
# STATE_CLOSE
###############################################################
        if smActiveState == STATE_CLOSE:
            if EVENT_DISTANCE_FAR == True:
                # ACTION:
                smAction_FAR()
                # TRANSITION:
                smActiveState = STATE_FAR                 
                # Reset event:
                EVENT_DISTANCE_FAR = False
                EVENT_TIMEOUT = False 
###############################################################
# STATE_FAR 
###############################################################
        elif smActiveState == STATE_FAR:
            if EVENT_DISTANCE_CLOSE == True:
                # ACTION: Insert your action code here:
                smAction_CLOSE()
                # TRANSITION:
                smActiveState = STATE_CLOSE 
                # Reset event:
                EVENT_DISTANCE_CLOSE = False
                EVENT_TIMEOUT = False 
        
    ###############################################################
    # Kald funktioner der tjekker for EVENTS
    ###############################################################
    checkEVENT_TIMEOUT()
    check_EVENT_DISTANCE() 
    # Add more EVENT checks as needed here...

    
