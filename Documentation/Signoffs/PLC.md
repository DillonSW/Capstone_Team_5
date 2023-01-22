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

Schematic 

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCSchemRevisionOne.jpg) 
 
Above is a draft schematic of how the PLC is going to be implemented into our machine. The LED resistor values can vary depending on what voltage the PLC's output is, and what kind of LED we decide to use. The typical output voltage of a PLC is 24VDC. Of course, this will be further discussed in the signoff for indication, but typical LED forward voltage can be from 1.2 - 3.6 V, with a typical current rating of 10 – 30 mA. 

^ Source: https://www.electronics-tutorials.ws/diode/diode_8.html 

The pins on the PLC are also tagged to their respective peripheral, and are specified as either an input (receiving from peripheral) or output (sending to peripheral) pin. The lock system shown is just for connection references, and will most likely need 2 pins per lock, as the PLC must constantly receive the state of the lock while also being able to increase or lower the voltage to the locks. The labels for the locking system state "Pin 1, 3, or 5" and "Pin 2, 4, or 6" because this same locking system will be used for all 3 locks. This will be discussed in the Security and Locks documentation. The same goes for the Distance Sensors system, and will be discussed in the sensor system documentation.

## Analysis 

To determine what LED resistance values are acceptable and expected, edge case analysis can be conducted. The equation for LED resistance is 

$Ω = (Vin – VLED)/ILED$

This is derived from Ohm's law, V = IR, and the circuit for an LED with a series resistor. 

![LEDCircuit](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/LEDAnalysis.jpg) 

Because an LED's forward voltage acts as a set voltage drop, a Kirchhoff Current Loop will yield:

$Vs - R(ILED) - VLED = 0$

Reorganized 

$(Vs – VLED)/ILED = R$

The following table shows the edge cases for resistor values. 

![ResistorValues](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/LEDResistors.jpg) 

## BOM 

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| Ethernet Cable | 5-ft, male-to-male, RJ45 Ethernet Cable | PLC | HL-001762 | Amazon Basics | 1 | $6.50 | $6.50 |
| PDA/Serial Adaptor Cable | 1.3-ft, USB-to-RS232 (DB9) Cable | PLC | NS-PU99501 | Insignia | 1 | $19.99 | $19.99 |
| 1766-L32BXB Allen Bradley | MicroLogix 1400 PLC | PLC | 1756-L32BXB | Allen Bradley | 1 | $601.40 | $601.40 |
| **Total** |  |  |  | **Total Components** | 3 | **Total Cost** | $627.89 |
