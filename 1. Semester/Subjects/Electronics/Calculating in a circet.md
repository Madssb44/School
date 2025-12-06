# Calculating in a circuit
## What is it?
When you have more than one Resistor/Capacitor/Inductor in a circuit you can calculate how the different values will be affected on the circuit before setting it up
## Why is it done?
Its done to ensure that you have the right amount of V,I,P e.t.c for the circuit you are calculating for as to not damage any components and to make it safe to make

## Terms
|Name|Symbol / Symbols
|:---:|:---:
|**Voltage & Volts**|$$V$$
|**Current & Amps**|$$I$$
|**Resistors & Ohms**|$$R \space/\space Ω$$
|**Power & Watts**|$$P \space/\space W$$
|**Total Amount**|$$T$$

## Formulas
|Device|Equivalent Series Connection|Equivalent Parallel Connection
|:---:|:---:|:---:
|Resistors|$$R_T = R_1+R_2+...+R_X$$|$$R_T=\frac{1}{(\frac{1}{R_1}+\frac{1}{R_2}+\frac{1}{R_3}+{etc...)}}$$
|Capacitors|$${C_T}=\frac{1}{\frac{1}{C_1}+\frac{1}{C_2}+\frac{1}{C_3}+etc...}$$|$$C_T=C_1+C_2+...+C_X$$
|Inductors|$$L_T=L_1+L_2+...+L_X$$|$${L_T}=\frac{1}{\frac{1}{L_1}+\frac{1}{L_2}+\frac{1}{L_3}+etc...}$$

## Important note!
Its important to always calculate in the direction the power is going to get the accurate readings needed to make sure you can use the calculations you have made
## Example
![alt text](<Pictures/circuit (1).png>)

The compleat formula for this circuit looks like this:
$${R_T} = R_1 + \left(\frac{1}{\frac{1}{R_2} +\frac{1}{R_3}}\right)$$

So to Find the resistance in the parallel we use the following formula:

$$R_T = \frac{1}{(\frac{1}{R_2}+\frac{1}{R_3})}$$

$$ \frac{1}{(\frac{1}{2,2kΩ}+\frac{1}{3,3kΩ})} = 1,32kΩ$$

Then we can do the entire circuit:

$$1k\spaceΩ + \left(\frac{1}{(\frac{1}{2,2kΩ}+\frac{1}{3,3kΩ})}\right) = 2,32k\spaceΩ$$
