## Subsystem Function 

The subsystem's role in our design is to control all electronic hardware (locks, LEDs, etc) as well as the motor rotating the platforms. It will also have a communication stream with the microcomputer to inform it when a board is checked out or restocked. 

## Constraints 

**The PLC:** 

* **Must have at least 6 Digital Input pins**

^ These are for the 3 door locks and sensors in order to be read by the PLC.

* **Must have at least 9 Digital Output pins**

^ These are also for the 3 door lock and sensors in order to be commanded by the PLC, in addition to the motor driver's Pulse (PUL) and Direction (DIR) ports.

^ Because all of the locks, sensors, and motor driver ports take 24VDC, the Digital Output (DO) ports will suffice for PLC commanding.

From this, the input module must have at least 6 ports, and the output module must have at least 9 ports 

* **Must be able to fit in a 3x1x1 foot area**

^ This is for clearance in the area where we are going to house all of our controllers and electronics, aside the motor. 

* **Will be in accordance with IEC-61131-2(6.4.4.3) which states:**

"When the short circuit (for a voltage output) or the open circuit (for a current output) is realized, no physical damage or abnormal phenomenon shall be detected." 

This will be accomplished by having a fuse breaker between the 24VDC supply and components.

^ Source: http://rpa.energy.mn/wp-content/uploads/2017/03/IEC-61131-2-Programmable-controllers-Equipment-Requirements-and-Tests.pdf 

* **Must be able to communicate with our PC and database**

^ This is discussed elsewhere; please refer to the Identification System

**These constraints will be numbered C1-C5 during Analysis**

## Schematic 

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Schematics/PLCSchemRevisionSeven.jpg) 
 
Above is a schematic of how the PLC is going to be implemented into our machine. The LED's in the schematic are rated to receive 24V AC/DC. Because of this there is no need for resistors to limit current to the LEDs. The 24VDC side is protected with a 15A fuse, and will be further discussed in Analysiss

The pins on the PLC are also tagged to their respective peripheral. DI a/b are Digital Input ports and DQ a/b are Digital Output ports.

**Discussion about the 120VAC side of the transformer will be in the Power System signoff. Please refer to it**

## Analysis 

**Constraints C1-C2**

^ The datasheet for the PLC states that it has "[Digital] 14 inputs/10 outputs"

^ Source: https://cache.industry.siemens.com/dl/files/465/36932465/att_106119/v1/s71200_system_manual_en-US_en-US.pdf

**Constraint C4**

^ This constraint is discussed elsewhere. Please refer to the Identification Subsystem.

**Constraint C3**

^ This constraint was given to us by the mechanical team as the approximated space that we would have for the electircal components in the back of the vending machine. The following images will show the area that the PLC takes up. The order is length, width, height. The dimensions will also be given below each image in inches and millimeters.

![PLCLength](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCLength.jpg)

PLC Length: 5.125 inches (130.175 mm)

![PLCDepth](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCDepth.jpg)

PLC Depth: 3 inches (76.2 mm)

![PLCHeight](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCHeight.jpg)

PLC Height: 4 inches (101.6 mm)

Given that our constraint is 3x1x1 feet, our PLC does meet this constraint.

* Constraint: **Will be in accordance with IEC-61131-2(6.4.4.3)**

To protect the 120VAC side of the system, we are using a GFCI cord and circuit breaker on the din rail (This is further discussed in the Power System signoff). To protect the 24VDC side, we must calculate the amount of current that will be drawn from each component. These values are already taking into account the x1.25 storage so that the current draw will not exceed 80% of the maximum. (Again, please refer to the Power System Signoff).

![PLCToDriver](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Schematics/PLCToDriver.jpg) 

The image above shows how the PLC is going to connect to the motor's driver. The driver's ports will receive 24VDC, hence why the PLC needed 24VDC output pins. The PLC will control the pulses (PUL +/-) and the direction (DIR +/-) of the driver, which will dictate how many pulses the motor will receive and what direction the motor will rotate.

^ Source: https://youtu.be/8hoBHmvRutA (This video is from an automation channel and shows, in great detail, how to connect a PLC to a stpper motor driver)

![Wiring](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Schematics/PLCWiring.jpg)

The image above shows how the PLC is wired internally to its inputs and outputs, and how it will be powered. The diagram shows that from a 24VDC power supply, the V- terminal will be connected to "M". The reason there are two wires is because the V- can act as the "ground" of the power supply, however it is still treated as V- and not common ground for the system. The V+ side will only be connected to "L".

^ Source: file:///C:/Users/ryanr/Downloads/technicalinfodoc_2702079%20(6).pdf

## BOM 

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| PL8B LED | 24V AC/DC LED | PLC | PL8B-24 | AlpineTech | 3 | $5.95 | $17.85 |
| Siemens S7-1200 PLC CPU | 14 Digital Input, 10 Digital Output | PLC | 6ES7214-1BE30-0XB0 | Siemens | 1 | $464.03 | $464.03 |
| **Total** |  |  |  | **Total Components** | 4 | **Total Cost** | $481.88 |
