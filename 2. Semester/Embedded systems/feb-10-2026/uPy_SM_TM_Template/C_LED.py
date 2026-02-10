from machine import Pin

#############################################################
# Module setup
#############################################################
LED_TASK_INTERVAL_MS = 10

#############################################################
# Local variables
#############################################################
listLED_config = []

#############################################################
# Hardware config
#############################################################
pinLED_PICO = Pin("LED", Pin.OUT)
# Add more LED pins here...

#############################################################
# Name definitions for the LEDs in the system
#############################################################
# LED names:
class LEDName:
    LED_PICO = 0 # The LED on the Pico PCB
# Add more LED names...

# LED MODES:
class LEDMode:
    LED_MODE_OFF = 0
    LED_MODE_ON = 1
    LED_MODE_BLINK = 2
    LED_MODE_FLASH = 3

# For private use in this module:
# Current LED state can be ON or OFF:
LED_OFF = 0
LED_ON = 1

# Index names for listLED_config[]
LED_INDEX_LED_NAME = 0
LED_INDEX_MODE = 1
LED_INDEX_STATE = 2
LED_INDEX_TIMER = 3
LED_INDEX_INTERVAL = 4
LED_INDEX_PIN = 5


#############################################################
# Public functions
#############################################################

###################################################################################################
# Brief         Initialize the LED list with all necessary parameters
#               Add your LED's in the system here.
#
# param[in]     None
# Return        None
#
# Warning       Must be called before usiong the LED module
###################################################################################################
def C_LED_Init():
    # Popularize list:
    
    # LED_PICO
    listTemp = [LEDName.LED_PICO, LEDMode.LED_MODE_OFF, LED_OFF, 0, 0, pinLED_PICO]
    listLED_config.append( listTemp )

    # Add other LED's in your system here...

###################################################################################################
# Brief         Set the MODE of a specific LED in the system  
#
# Param[in]     iLED:           The name of the LED (LED_PICO...)
#               iMode:          The new mode (LED_MODE_BLINK...)
#               iInterval_ms:   If iMode is BLINK or FLASH, this value is the interval
# Return        None
#
# Warning       None
###################################################################################################
def C_LED_SET_MODE( iLED: int, iMode: int, iInterval_ms: int):
    listTemp = listLED_config[iLED]
    listTemp[LED_INDEX_MODE] = iMode
    listTemp[LED_INDEX_STATE] = LED_OFF
    listTemp[LED_INDEX_TIMER] = 0
    listTemp[LED_INDEX_INTERVAL] = iInterval_ms

    listLED_config[iLED] = listTemp


###################################################################################################
# Brief         This task takes care of controlling the LED's, by turning the LED ON or OFF
#               depending on the LED mode.
#               Decrements the timer for each LED, when the mode is set to blinking/flashing
#               Supports these modes currently: OFF, ON, BLINK, FLASH
# Param[in]     None
# Return        None
#
# Warning      Must be called every LED_TASK_INTERVAL_MS ms
###################################################################################################
def C_LED_Task():
    # For each LED in the list:
    # - Decrement timer
    # - Check if the LED must be ON or OFF, depending on the MODE
    # - Turn LED ON or OFF
    for thisLED in listLED_config:
        # Decrement timers:
        if thisLED[LED_INDEX_TIMER] > 0:
            thisLED[LED_INDEX_TIMER] -= LED_TASK_INTERVAL_MS

        # Set the LED state to ON or OFF:
        if thisLED[LED_INDEX_MODE] == LEDMode.LED_MODE_OFF:
            thisLED[LED_INDEX_STATE] = LED_OFF
        elif thisLED[LED_INDEX_MODE] == LEDMode.LED_MODE_ON:
            thisLED[LED_INDEX_STATE] = LED_ON
        elif thisLED[LED_INDEX_MODE] == LEDMode.LED_MODE_BLINK:
            # If the timer has timed out, toggle the LED state:
            if thisLED[LED_INDEX_TIMER] <= 0:
                # Timeout. Now toggle the LED:
                if thisLED[LED_INDEX_STATE] == LED_OFF:
                    thisLED[LED_INDEX_STATE] = LED_ON
                else:
                    thisLED[LED_INDEX_STATE] = LED_OFF
                # Reset the timer value:
                thisLED[LED_INDEX_TIMER] = thisLED[LED_INDEX_INTERVAL]
        elif thisLED[LED_INDEX_MODE] == LEDMode.LED_MODE_FLASH:
            # If the timer has timed out, toggle the LED state:
            if thisLED[LED_INDEX_TIMER] <= 0:
                # Timeout. Now toggle the LED:
                if thisLED[LED_INDEX_STATE] == LED_OFF:
                    thisLED[LED_INDEX_STATE] = LED_ON
                else:
                    thisLED[LED_INDEX_STATE] = LED_OFF
                # Reset the timer value:
                if thisLED[LED_INDEX_STATE] == LED_OFF:
                    thisLED[LED_INDEX_TIMER] = thisLED[LED_INDEX_INTERVAL] - 50
                else:
                    thisLED[LED_INDEX_TIMER] = 50

        # Set PIN (turn the LED ON or OFF:)
        thisLED[LED_INDEX_PIN].value(thisLED[LED_INDEX_STATE])

