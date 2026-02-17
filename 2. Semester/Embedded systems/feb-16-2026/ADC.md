# notes for today 

## ADC
ADC stands for analog to digital convertion 

what it does is it converts a reading from a analog signal a microcontraler measures in bits (12 bit) 
and converts it to a digital value

## On a Pico 
you can do this on our pico by:

so by setting up a circuit that can take all the voltage of the battery and spread it over the avalibale analog pins
you can then take the power supplys output and direct it through the circuit and make a analog reading on each of the pins

then by finding out how many bits your microchip can handle and dividing that by how much voltage the pins can take you can find out
what 1 us of pulse from the analog signal equatets to in voltage, then by reading on all the pins adding them together
and then multplying them with your single 1us voltage value you can get the total voltage given by the battery

you just need to make sure all your pins max readings can take the maximum output of the battery otherwise you wont be able
to measure the total for obvious reasons 

## On a breakout board
While not being able to get the accurate reading you can make a indicator of how much voltage your battery outputs by:

Making a circuit there you take the power form the battery in on one side then having a serial circuit consiting of
led lamps and resistors spreading the voltage out over how many leds you want by making the resistors equal ohms

whan will happen here is that the lower the voltage will be the fewer of the leds will light up, allowing you to make 
a circuit where you have a total number of leds that will light up thew the battery is at full capacity and then slowly
turning off more leds the less voltage is left on the battery and using that as the indicator of how much power you have left

