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

* **Must be able to communicate with our PC**
^ (The information about communication are also discussed in the Sensor System signoff)
To remove data from the computer for use, a program will be added to the PC so when the drive is plugged in, the information is downloaded automatically. The port will be behind a locked compartment so students cannot access the data.

To connect the Computer to the PLC, a USB NIC will be needed to provide an extra Ethernet port. The PLC uses Profinet, which is a communication protocol used to collect information and control a PLC through Profibus. The Computer will use an application called TIA Portal which allows connection and communication with the PLC and functions as a controller for S7 1200 and 1500 series PLCs. To use the TIA portal software, the PLC needs a minimum of 16 GB of RAM and an Intel Core i5-8400H or stronger CPU. The ThinkCentre provides enough RAM and a strong enough CPU to handle the program. The program will be created in the TIA portal and loaded to the memory on the PLC. TIA portal also provides diagnostics of the PLC through the software. The PLC the team is using is called a SIMATIC S7 1200 from Siemens and requires certain types of memory card. The three options of memory for the PLC differ only by capacity. The three options for memory size are 2, 4, and 24 MB. The team is using a 4MB memory card for the PLC since the 2MB is out of production. Issues have arrived with a USB NIC not being recognized by TIA Portal. If the software does not recognize the NIC, the way to fix the issue is to enter the IP address manually. The TIA Portal SIMATIC Step 7 program allows the use of an OPC UA Server.

^ Source: https://us.profinet.com/profinet-explained/, https://support.industry.siemens.com/cs/document/109784439/delivery-release-simatic-step-7-professional-basic-v17?dti=0&lc=en-WW

To retain information from the PLC and PC, an OPC UA client from Prosys will be used. The OPC client allows the PLC to connect and send/receive data to/from the database. The database will be accessible to the PC as well. The database will be the interface between the PC and PLC. The PC will be able to set bits high to activate the PLC, and the PLC will be able to set the bits low after completion of the job. The OPC client is designed to be used with SIMATIC S7 1200 and 1500 series PLCs, and connect to the MySQL database software. The Prosys OPC client can connect directly to the Server created in the TIA portal software and then relay the information to the database for use by the PC and vice versa.

^ Source: https://downloads.prosysopc.com/opcua/apps/JavaClient/dist/3.2.0-328/Prosys_OPC_UA_Client_UserManual.pdf

## Schematic 

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-Signoff-PLC/images/PLCSchemRevisionThree.jpg) 
 
Above is a draft schematic of how the PLC is going to be implemented into our machine. The LED's in the schematic are rated to receive 24V AC/DC. Because of this there is no need for resistors to limit current to the LEDs.

The pins on the PLC are also tagged to their respective peripheral. DI a/b are Digital Input ports and DQ a/b are Digital Output ports.

## Analysis 

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
