## Subsystem Function 

The subsystem's role in our design is to control all electronic hardware (locks, LEDs, etc) as well as the motor rotating the platforms. It will also have a communication stream with the microcomputer to inform it when a board is checked out or restocked. 

## Constraints 

**The PLC:** 

* **Must have at least 6 Digital Input pins**

^ These are for the 3 door locks and sensors in order to be read by the PLC.

* **Must have at least 6 Digital Output pins**

^ These are also for the 3 door lock and sensors in order to be commanded by the PLC.

* **Must have at least 3 24VDC Outputs**

^ These are going to be used for the motor driver.

From this, the input module must have at least 6 ports, and the output module must have at least 9 ports 

* **Must be able to fit in a 3x1x1 foot area**

^ This is for clearance in the area where we are going to house all of our controllers and electronics, aside the motor. 

* **Will be in accordance with IEC-61131-2(6.4.4.3) which states:**

"When the short circuit (for a voltage output) or the open circuit (for a current output) is realized, no physical damage or abnormal phenomenon shall be detected." 

This will be accomplished by having the GFCI in between our hardware and the power supply. 

^ Source: http://rpa.energy.mn/wp-content/uploads/2017/03/IEC-61131-2-Programmable-controllers-Equipment-Requirements-and-Tests.pdf 

* **Must be able to communicate with our PC and database**

## Schematic 

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCSchemRevisionThree.jpg) 
 
Above is a draft schematic of how the PLC is going to be implemented into our machine. The LED's in the schematic are rated to receive 24V AC/DC. Because of this there is no need for resistors to limit current to the LEDs.

The pins on the PLC are also tagged to their respective peripheral. DI a/b are Digital Input ports and DQ a/b are Digital Output ports.

## Analysis 

* Constraint: **Must be able to communicate with our PC and database**

^ This constraint is discussed elsewhere. Please refer to the Identification Subsystem.

* Constraint: **Must be able to fit in a 3x1x1 foot area (LxWxH)**

^ This constraint was given to us by the mechanical team as the approximated space that we would have for the electircal components in the back of the vending machine. The following images will show the area that the PLC takes up. The order is length, width, height. The dimensions will also be given below each image in inches and millimeters.

![PLCToDriver](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCToDriver.jpg) 

The image above shows how the PLC is going to connect to the motor's driver. The driver's ports will receive 24VDC, hence why the PLC needed 24VDC output pins. The PLC will control the pulses (PUL +/-) and the direction (DIR +/-) of the driver, which will dictate how many pulses the motor will receive and what direction the motor will rotate.

![Wiring](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCWiring.jpg)

The image above shows how the PLC is wired internally to its inputs and outputs, and how it will be powered. The diagram shows that from a 24VDC power supply, the V- terminal will be connected to both "M" (which can be the local ground/neutral) and the PLC's ground terminal. The V+ side will only be connected to "L".

^ Source: file:///C:/Users/ryanr/Downloads/technicalinfodoc_2702079%20(6).pdf

## BOM 

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| PL8B LED | 24V AC/DC LED | PLC | PL8B-24 | AlpineTech | 3 | $5.95 | $17.85 |
| Siemens S7-1200 PLC CPU | 14 Digital Input, 10 Digital Output | PLC | 6ES7214-1BE30-0XB0 | Siemens | 1 | $464.03 | $464.03 |
| **Total** |  |  |  | **Total Components** | 4 | **Total Cost** | $481.88 |
