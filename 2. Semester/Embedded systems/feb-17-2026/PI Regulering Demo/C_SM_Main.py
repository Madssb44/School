from C_LED import C_LED_SET_MODE, LEDName, LEDMode
from C_RobotCar import *
from D_GY53 import *

#############################################################
# Module setup
#############################################################
SM_TICK_MS = 100

#############################################################
# Name definitions used by the Statemachine
#############################################################
# SM STATES:
STATE_CLOSE                  = 0
STATE_FAR                  = 1

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
def smAction_A():
    # Example code. Insert your own ACTION code
    C_LED_SET_MODE( LEDName.LED_PICO, LEDMode.LED_MODE_BLINK, 500 )
    smSetTimeout_sec( 5 )

###################################################################################################
# Brief         Action B for the statemachine
#
# Param[in]     None
# Return        None
#
# Warning       None
###################################################################################################
def smAction_B():
    # Example code. Insert your own ACTION code
    C_LED_SET_MODE( LEDName.LED_PICO, LEDMode.LED_MODE_FLASH, 500 )
    smSetTimeout_sec( 5 )

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
# Warning       Must be called every time the Statemachine is called
###################################################################################################
def checkEVENT_DISTANCE():
    global EVENT_DISTANCE_CLOSE, EVENT_DISTANCE_FAR

    # I state CLOSE tjekker vi om bilen er kommet mere end 30 cm væk fra muren
    if smActiveState == STATE_CLOSE:
        if D_GY53_GetDistance() > 300:
            EVENT_DISTANCE_FAR = True
            EVENT_DISTANCE_CLOSE = False
    # I state FAR tjekker vi om bilen er kommet tættere end 20 cm fra muren
    elif smActiveState == STATE_FAR:
        if D_GY53_GetDistance() < 200:
            EVENT_DISTANCE_FAR = False
            EVENT_DISTANCE_CLOSE = True


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
    smAction_A()
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
    global EVENT_DISTANCE_CLOSE
    global EVENT_DISTANCE_FAR

    ###############################################################
    # STATE_CLOSE
    ###############################################################
    if smActiveState == STATE_CLOSE:
        if EVENT_DISTANCE_FAR == True:
            # ACTION:
            smAction_A()
            # TRANSITION:
            smActiveState = STATE_FAR                
            # Reset event:
            EVENT_DISTANCE_FAR = False

    ###############################################################
    # STATE_B
    ###############################################################
    elif smActiveState == STATE_FAR:
        if EVENT_DISTANCE_CLOSE == True:
            # ACTION: Insert your action code here:
            smAction_B()
            # TRANSITION:
            smActiveState = STATE_CLOSE
            # Reset event:
            EVENT_DISTANCE_CLOSE = False

    ###############################################################
    # Kald funktioner der tjekker for EVENTS
    ###############################################################
    checkEVENT_TIMEOUT()
    checkEVENT_DISTANCE()
    # Add more EVENT checks as needed here...
