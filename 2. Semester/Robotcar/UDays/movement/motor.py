from machine import Pin, PWM


# left motor has 4 offset
# Pins for right motor 16 17 18
# Pins for left motor 19 20 21


class DCmotor:
    """DC Motor class
    class made for a dc motor with 2 pins and a pwm pin

    Defaults: 
        max_duty & min_duty are preset for a raspberry pi pico's arcitecture
        speed is set to 0 so the motor doesnt start when making the object 

    Attributes:
        pos_pin: possitive pin for the motor  
        neg_pin: negetive pin for the motor 
        enable_pin: pwm enable pin for the motor 
        max_duty: max duty, depends on arcitecture 
        min_duty: min_duty, ensures the motor gets the minimum duty needed to spin
        speed: sets the standart speed

    Methods: forward, backward, stop, custome
    """
    def __init__(self, pos_pin, neg_pin, enable_pin, max_duty=65636, min_duty=20000, speed=0):
        self.pos_pin = Pin(pos_pin, Pin.OUT)
        self.neg_pin = Pin(neg_pin, Pin.OUT)
        self.enable_pin = PWM(enable_pin, freq=1000, duty_u16=65535)
        self.max_duty = max_duty
        self.min_duty = min_duty
        self.speed = speed


    def duty_cycle(self, speed) -> int:
        """Calculates the duty from a int between 1-100

        Param: speed
        Return: duty
        Warning: speed needs to be a int """
        if self.speed <= 0 or self.speed > 100:
            duty_cyclen = 0
        else:
            duty_cyclen = int(self.min_duty + (self.max_duty - self.min_duty) * ((self.speed - 1) / (100 - 1)))

        return duty_cyclen

    def forward(self, speed):
        self.speed = speed
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pos_pin.on()
        self.neg_pin.off()

    def backward(self, speed):
        self.speed = speed
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pos_pin.off()
        self.neg_pin.on()

    def stop(self):
        self.enable_pin.duty_u16(0)
        self.pos_pin.on()
        self.neg_pin.on()

    def custom(self, pos_pin:int, neg_pin:int, speed):
        self.enable_pin.duty_u16(speed)
        self.pos_pin.value(pos_pin)
        self.neg_pin.value(neg_pin)


class Car:
    """Class for Car
    with 2 DCmotors with pwm control 
    

    Defaults:
        r_offset: can be set if the right motor needs offset
        l_offset: can be set if the left motor needs offset 
    
    Attributes:
        r_pos_pin: right possitive pin
        r_neg_pin: right negative pin 
        l_pos_pin: left possitive pin 
        l_neg_pin: left negative pin 
        r_enable_pin: enable pin for right motor
        l_enable_pin: enable pin for left motor  
        offset: offset for right motor 
        offset: offset for left motor 
    
    Methods: move_forward, move_backward, turn_right, turn_left, q_turn_right, q_turn_left, stop
        """
    def __init__(self, r_pos_pin:int, r_neg_pin:int, r_enable_pin:int, l_pos_pin:int, l_neg_pin:int, l_enable_pin:int,  r_offset=0, l_offset=0):
        self.r_pos_pin = r_pos_pin
        self.r_neg_pin = r_neg_pin
        self.r_enable_pin = r_enable_pin 
        self.l_pos_pin = l_pos_pin
        self.l_neg_pin = l_neg_pin
        self.l_enable_pin = l_enable_pin
        self.r_offset = r_offset
        self.l_offset = l_offset
        self.right_motor = DCmotor( self.r_pos_pin, self.r_neg_pin, self.r_enable_pin )
        self.left_motor = DCmotor( self.l_pos_pin, self.l_neg_pin, self.l_enable_pin )


    def move_back( self, speed ): 
        self.right_motor.forward( int(speed - self.r_offset ))
        self.left_motor.backward( int(speed - self.l_offset ))


    def stop( self ):
        self.right_motor.stop()
        self.left_motor.stop()


    def move_forward( self, speed ):
        self.right_motor.forward( int( speed - self.r_offset ))
        self.left_motor.forward( int( speed - self.l_offset ))


    def turn_right(self, speed ):
        self.right_motor.forward(( int( speed - self.r_offset ) / 2))
        self.left_motor.forward( int( speed - self.l_offset ))


    def q_turn_right(self, speed = 50 ):
        self.right_motor.backward( int( speed - self.r_offset ))
        self.left_motor.forward( int( speed - self.l_offset ))


    def turn_left( self, speed ):
        self.right_motor.forward( int( speed - self.r_offset ))
        self.left_motor.forward(( int( speed - self.l_offset ) / 2 ))

    def q_turn_left( self, speed = 50 ):
        self.right_motor.forward( int( speed - self.r_offset ))
        self.left_motor.backward( int( speed - self.l_offset ))

    def custom_movement( self, r_pos_val:int, r_neg_val:int, l_pos_val:int, l_neg_val:int, r_speed:int, l_speed:int ):
        self.right_motor.custom( r_pos_val, r_neg_val, r_speed )
        self.left_motor.custom( l_pos_val, l_neg_val, l_speed )





