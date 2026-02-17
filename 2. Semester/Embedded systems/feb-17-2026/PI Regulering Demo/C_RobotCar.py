#from machine import Pin
import time
from servo import Servo

from D_GY53 import *

#############################################################
# Module setup
#############################################################
# Setup regulation parameters
REG_SETPOINT_DISTANCE_MM = 200.0    # Setpoint
P_VALUE = 1.0                       # P-value
I_VALUE = 0.0                       # I-value

# Simulering af at robotbilen ikke kører 100% lige ud når vi tror det.
CAR_DIRECTION_ERROR_DEG = 0.0   # 0.0 = Ideel scenarie, hvor
                                # bilen kun 100% nøjagtigt ligeud

#############################################################
# Hardware config
#############################################################
my_servo = Servo(pin_id = 15)

#############################################################
# Local variables
#############################################################
# I integration value:
fI_sum = 0.0

# Variable used to calculate a simulated distance, based on current wheel angle:
fDistanceSimul_mm = 0

# Misc variables:
fServoPosition_deg = 90.0
fDistanceError_mm = 0.0

#############################################################
# Name definitions
#############################################################

###################################################################################################
# Public functions
###################################################################################################


###################################################################################################
# Brief         Init function
#
# Param[in]     None
# Return        None
#
# Warning       Must be called at power up
###################################################################################################
def C_RobotCar_Init():
    print("RobotCar Initialized")

###################################################################################################
# Brief         
#
# Param[in]     
# Return        None
#
# Warning       None
###################################################################################################
def C_RobotCar_Task():
    global fServoPosition_deg
    global fDistanceSimul_mm, fDistanceError_mm
    global fI_sum

     # Beregn fejl ift setpunkt:
    fDistanceError_mm = REG_SETPOINT_DISTANCE_MM - fDistanceSimul_mm

    # Beregn I-led:
    # Sum (integrale) af fejlen over tid:
    fI_sum = fI_sum + I_VALUE * fDistanceError_mm
    # Beregn nu vinkel baseret på P og I led
    # Rat vinkel = P     * Fejl              + I * Summeret fejl
    fSteeringWheelAngle = P_VALUE * fDistanceError_mm + fI_sum
    fSteeringWheelAngle = -fSteeringWheelAngle

    # TODO Her burde vi sørge for at vi kun sætter ønsket vinkel mellem f.eks. +/- 45 grader, eller hvor skarpt det giver mening at dreje.

    print( f"Afstand = {fDistanceSimul_mm:5.1f} mm Fejl = {fDistanceError_mm:5.1f} mm - Ratvinkel = {fSteeringWheelAngle:5.1f} grader")
    # Beregn ny simuleret afstand baseret på ratvinkel: 
    fDistanceSimul_mm = fDistanceSimul_mm - 0.2*(fSteeringWheelAngle + CAR_DIRECTION_ERROR_DEG)

    ##########################################
    # Sæt servo motor position:
    ##########################################
    # Servo kan sættes fra 0 - 180 grader, hvor 90 grader er lige ud for vores bil:
    # Når Ratvinkel er negativ -> drejer mod venstre.
    # Vi må bruge den negative værdi af fSteeringWheelAngle
    fServoPosition_deg = -fSteeringWheelAngle + 90.0
    # Vi skal sikre at vi holder is inden for 0-180 grader:
    # For en sikkerhedskyld holder vi os indenfor 5-175 grader.
    # Det giver ikke mening at dreje skarpere alligevel
    if fServoPosition_deg < 5.0:
        fServoPosition_deg = 5.0
    elif fServoPosition_deg > 175.0:
        fServoPosition_deg = 175.0

    # Sæt servo/rat position:
    my_servo.write( fServoPosition_deg )

###################################################################################################
# Brief         
#
# Param[in]     
# Return        None
#
# Warning       None
###################################################################################################
def C_RobotCar_SetServoZero():
    my_servo.write( 0 )

###################################################################################################
# Brief         
#
# Param[in]     
# Return        None
#
# Warning       None
###################################################################################################
def C_RobotCar_GetSteeringWheelAngle():
    return fServoPosition_deg
