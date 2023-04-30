# Class Kit Vending Machine 

## Executive Summary

Every year hundreds of students require various devices for their ECE (Electrical and Computer Engineering) classes. These specific devices are provided by the College of Engineering and are rented out to students through the ECE office. Typically, in the first month of a semester, students attempt to check out on average 50 devices in a day from the Office. This capstone project will focus on designing and implementing a vending machine that can distribute devices out to students while recording which students have checked out a device. The finished product will be a vending machine with the functionality to vend the needed specific devices to students. A student can enter their information into the machine, and the machine will record who has checked out their respective device(s). The machine will use a motor to rotate a device to the door for a student to remove that has LEDs (Light Emitting Diode) which will allow students to see and determine which device is the one they should remove. The student will then take the device and shut the door for the next student.     

## Capabilities

The first prototype of the vending machine has the capability to record all input student data and store to the SQL database held on the host machine. The program can communicate using custom OPC software and read/write tags to turn the motor. The GUI has a loading mode where the admin can enter all devices inside the machine and a delete mode where all data held by the database can be removed. After loading, the machine resets to the initial position to track exactly which board will be rented. The motor is powered through the custom enclosure and is controlled by the PLC. The overall function of the machine allows a student to enter data and quickly receive a response from the machine, returning a board to the student and recording exactly which device was given.  

## Salient Outcomes

In progress...

## Project Demonstration & Images

Experimentation Videos:
* GUI system: https://youtu.be/tVvsogPO3sM  
* Safety System: https://youtu.be/iVfy9IWk9oA  
* PLC System: https://youtu.be/Vv9zIDt42ac  

**GUI Image**  

![GUI](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/GUI.jpg)  

**Enclosure Image**  

![Enclosure](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Enclosure.jpg)  

**Safety System and PLC Image**  

![Safety/PLC](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Safety_PLC.jpg)  

## Subsystems
* Identification
* Safety
* UI
* Power
* Sensors
* Motor
* PLC
* Security  

## About Us  

![TeamPhoto](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/TeamPhoto.jpg)  

**Left to Right: Michel Turpeau, Ryan Reed, Dillon Williams, Nidhay Patel, Austin Sigg**  

This team consists of three Electrical Engineers and two Computer Engineers. The three Electrical Engineers are Austin Sigg, Ryan Reed, and Michel Turpeau. The two Computer Engineers are Dillon Williams and Nidhay Patel. The Class Kit Vending Machine is being designed to make the process of renting class devices faster while giving our customers more time for their own responsibilities.  

### Faculty Supervisor

Our faculty supervisor is Dr. Jesse Roberts

### Stakeholders

Our customers are the associates working in the ECE (Electrical and Computer Engineering) office of Brown Hall at Tennessee Tech University.  
The machine should allow more time for associates to complete other responsibilities without being interrupted by students as often.  

### Recognitions

Our Team would like to recognize our partnered Mechanical Engineering Team for their help. The team consists of:  
Carson Pitts, Jessee Millsaps, Mason Baines, and Nathan Bangean.

## Repo Organization

* The Team Contract is present in main  


### Reports

* Conceptual Design and Revisions  
* Project Proposal and Revisions  
* Experimentation
* Lessons Learned

### Documentation

* 3D Models
* Electrical
  * Sources
  * Schematics
* Images
  * 3D Models
  * Schematics
  * Software
* Signoffs

### Software

* Database
* Klaw_rev3
* OPC_rev2
* PLC

