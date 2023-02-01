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

* **Must be able to fit in a 1 square-foot area**

^ This is for clearance in the area where we are going to house all of our controllers and electronics, aside the motor. 

* **Will be in accordance with IEC-61131-2(6.4.4.3) which states:**

"When the short circuit (for a voltage output) or the open circuit (for a current output) is realized, no physical damage or abnormal phenomenon shall be detected." 

This will be accomplished by having the GFCI in between our hardware and the power supply. 

^ Source: http://rpa.energy.mn/wp-content/uploads/2017/03/IEC-61131-2-Programmable-controllers-Equipment-Requirements-and-Tests.pdf 

* **Must be able to communicate with our PC
^ This is discussed in other signoffs; we plan to use the ethernet ports on the PLC and a software on our PC similar to Rockwell.

Schematic 

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCSchemRevisionThree.jpg) 
 
Above is a draft schematic of how the PLC is going to be implemented into our machine. The LED resistor values can vary depending on what voltage the PLC's output is, and what kind of LED we decide to use. The typical output voltage of a PLC is 24VDC. Of course, this will be further discussed in the signoff for indication, but typical LED forward voltage can be from 1.2 - 3.6 V, with a typical current rating of 10 – 30 mA. The 2.2 kOhm resistors going to the driver are to help prevent current overflow.

^ Source: https://www.electronics-tutorials.ws/diode/diode_8.html 

The pins on the PLC are also tagged to their respective peripheral, and are specified as either an input (receiving from peripheral) or output (sending to peripheral) pin. The lock system shown is just for connection references, and will most likely need 2 pins per lock, as the PLC must constantly receive the state of the lock while also being able to increase or lower the voltage to the locks. The labels for the locking system state "Pin 1, 3, or 5" and "Pin 2, 4, or 6" because this same locking system will be used for all 3 locks. This will be discussed in the Security and Locks documentation. The same goes for the Distance Sensors system, and will be discussed in the sensor system documentation.

## Analysis 

![PLCToDriver](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCToDriver.jpg) 

The image above shows how the PLC is going to connect to the motor's driver. The driver's ports will receive 24VDC, hence why the PLC needed 24VDC output pins. The PLC will control the pulses (PUL +/-) and the direction (DIR +/-) of the driver, which will dictate how many pulses the motor will receive and what direction the motor will rotate.

## BOM 

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| PL8B LED | 24V AC/DC LED | PLC | PL8B-24 | AlpineTech | 3 | $5.95 | $17.85 |
| Siemens S7-1200 PLC CPU | 14 Digital Input, 10 Digital Output | PLC | 6ES7214-1BE30-0XB0 | Siemens | 1 | $464.03 | $464.03 |
| **Total** |  |  |  | **Total Components** | 4 | **Total Cost** | $481.88 |
