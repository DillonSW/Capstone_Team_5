# Experimental Analysis  
 
## Identification Subsystem 

### Purpose of the subsystem  
---
The purpose of the subsystem is to store student information into a database and automatically assign the student the correct board depending on class selection. The system has not met all of the original constraints due to issues obtaining the part orders. It is important to note that the original specifications have been met in another way.  

The customer required the program to do a few things: store the student ID, name, email, class, and term, before ordering the machine to bring the appropriate device to the door.  

Most of the constraints enumerated in the signoff have not been met due to parts never arriving for the team, however, the constraints have been partially satisfied by substituting the needed hardware with software. Any other constraints where parts were not received and not able to be programmed are considered out of the scope of this project.  

---
### Constraints/Specifications
---
Below is a list of the constraints for the ID system. They are numbered C1 to C9

C1: Barcode Scanners shall be low power and consume no greater than 5 V 0.5 A.  

C2: Barcode Scanners shall be able to decode Code-128 barcodes  

C3: Barcodes shall be of decent quality to follow ISO 15416 standard. Assures that the codes can be read by any scanner  

C4: RFID Card Scanner shall be low power and consume no greater than 5 V 0.5 A

C5: RFID Card Scanner shall operate on 13.56 MHz commonly used for higher security access badges, like the school Eagle Cards  

C6: A Barcode Scanner and Card Reader will be monitered by USB voltmeter to ensure correct operation  

C7: The PC shall run on Windows 10 to provide the needed applications for PLC and Database  

C8: The PC will provide an ethernet port to communicate with the PLC through a USB NIC (network interface card)  

C9: The PC will provide at minimum an Intel Core i5-8400H or stronger CPU and 16GB RAM to support PLC programs  

Constraints C1-C3 required a barcode scanner that could scan the boxes and use a required rating of 5V, 0.5A. Since the scanner was never received by the team, the application now allows the customer to enter codes manually through the GUI application. The program still automatically assigns the board as originally required. 

Constraints C4-C6 required the RFID scanner to read data off the school ID card and automatically fill the database with the student ID. Since the scanner was never received, the program now has the student enter his/her own ID and error checking the entered information and the Voltmeter is no longer required without the 2 scanners. 

Constraints C7-C9 required the team to have a decently rated Windows 10 computer for running the PLC, GUI, and database, but due to IT policies, the computer was not allowed to be purchased by the school. Instead, the school provided a Linux PC for the team to use for programming. The PLC application was used from the school lab due to never receiving the memory card for our acquired PLC. 

---
### Experimental Procedure  
---
To test this subsystem, a user entered data through the GUI and it was verified to be inside of the database on the host with the correct assigned board. The inventory entered in the program was also verified to be inside the database. The running of the motor will be demonstrated in the PLC analysis, and the Error checking will be shown in the GUI analysis. 

---
### Expected Results  
---
The team expected the student data to be in the database in alphabetical order along with the rented board determined by the step count handled by the program. The inventory was also expected to be present with its rented and stored date because a student cannot rent without a device in the machine.
A total of 10 random students were entered into the database along with 15 random devices. 

---
### Collected Data
---
Constraint C1 is unable to be met in the original way to do unforseen ordering circumstances. Instead, the team has allowed the manual entry of boxnumbers through the GUI system. The results can be shown in the third figure below where the numbers are inside of the database after entry.  

Constraint C2 has been deemed out of scope by the team due to never receiving the barcode scanner as mentioned for C1.  

For Constraint C3, barcodes were never made since the barcode scanner was not received. The devices can instead be entered by the boxnumber written on the device.  

Constraint C4 is unable to be met in the original way to do unforseen ordering circumstances. Instead, the team has allowed the manual entry of Student ID numbers through the GUI system. The results can be shown in the second figure below where the IDs are inside of the database after entry.  

Constraint C5 has been deemed out of scope by the team due to never receiving the Card reader as mentioned for C4.  

The USB Voltmeter was never received and therefore C6 cannot be tested. 

Constraint C7 is not met due to ordering restrictions with the IT department. Instead, a Linux PC with the appropriate specifications was provided by the college.  

Constraint C8 has been deemed out of scope due to never receiving the USB NIC from the placed order forms. 

For testing C9, the team went into the specifications of the PC provided by the college to verify that the CPU and Memory. 

![SpecsPC](https://github.com/DillonSW/Capstone_Team_5/blob/main/images/CapstonePC_Specs.png)  

As you can see in the photo above, the CPU is stronger than an Intel Core i5 and the Memory is 16 GB.

Below you can see the results of running the database program while taking input from the GUI. The database needed to hold all 10 test entries in the student database and keep track of the rented device and student information. 

![Students_Results](https://github.com/DillonSW/Capstone_Team_5/blob/main/images/Students_Results.png)  

Below you can see the results of the inventory table after testing the entry of 15 devices and the renting of 10. The devices should be removed in order of entry into the machine.  

![Inventory_Results](https://github.com/DillonSW/Capstone_Team_5/blob/main/images/Inventory_Results.png)  

---
### Data Interpretation
---

---
### Future Improvements
---

## GUI Subsystem

### Purpose of the subsystem
---
The purpose of the graphic user insterface is to take information from the user and store it into the database through the ID subsystem. The interface allows for a convenient way to rent a device for a class and provides error checking to verify information is in the correct format.

The interface is able to let a user input information into the ID subsystem and provide the student with notifications while renting a device. The GUI must follow certain constraints determined during the design of the project. The team was not able to order a touchscreen for the project, but received a ubuntu 20.04 computer from the school IT department instead. 

Constraints C1-C3 are satisfied by the computer provided to the team by the IT department. 

Constraint C4 was satisfied by a personal laptop of a team member, where he programmed a custom PLC ladder logic program. 

Constraint C5 will need to be improved upon in the next rendition of the design by a future capstone team. Due to a lack of parts, the machine will not be moved into the Brown student lounge, so an anchored PC was not needed. 

---
### Experimental Procedure
---
To test this subsystem, a user entered incorrect data and correct data into the UI to verify the operation of error checking. The UI will provide popups whenever it detects and error, and will not take any data until the error is resolved. The data will be checked to make sure incorrect data was not entered into the database. There is operations in the code to prevent SQL injection into the database, which will be verified by trying to inject through the GUI input box. There is a command that will shut down the program as well and will be tested after data is entered. 

---
### Expected Results
---
The team expected to see all errors popup during the correct time and allow data storage when the GUI was not faced with an error. The GUI was also expected to prevent incorrect data from being stored during an error and prevent injection through the input box located on the screen. Every error was checked by first entering correct data, then inputting incorrect data to the ID system through the GUI. The team also attempted to inject a query through each input box twice in case a first attempt catches an error. 

---
### Collected Data
---



---
### Data Interpretation
---

---
### Future Improvements
---

## PLC System

### Purpose of the Subsystem
---
The purpose of the PLC system is to be the middle-man between our database and our physical peripherals such as the motor and LEDs. The reason we chose to use a PLC in addition to a Linux PC is because PLCs are designed to handle physical control faster and more efficiently than a PC.

Constraints C1 and C2 required us to have the memory card for our PLC, which does satisfy these constraints. But, due to ordering issues, we are using the PLCs in our PLC lab, which have 8 digital input and outputs. So, with what we have, C1 is satisfied but C2 is not.

Constraint C3 is satisfied, even with the ordering issues. The PLC setup that we are using is 24-inches long, and less than 6-inches deep and tall. So, our system will fit within a 3x1x1 foot area, and C3 is satisfied.

Constaint C4 is satisfied with the PLC we are using. The PLCs in the lab have two 48V fuses, one that is rated for 2A and the other for 4A. This satisfies IEC-61131-2(6.4.4.3) for protection from physical damage.

Constraint C5 is satisfied by the use of a custom OPC client that can read-from and write-to the PLC.

---
### Experimental Procedure
---
To test this subsystem, we connected the only peripheral we have available to us, the motor driver, and aliased its inputs (STEP, DIR) with tags in the PLC. When these tags are energized and unenergized, the motor should be able to step and change direction based on the state of their respective tags. Because most of the constraints revolving around the PLC are about its peripherals, there are not many constraints that can be experimented on in this section.

---
### Expected Results
---
If everything is connected properly, and the OPC client can ping to the PLC, the OPC should be able to change the state of a tag and read its state. The PLC should also be able to revert the state of the tag changed by the OPC for the next run.

---
### Collected Data
---

---
### Further Improvements
---

## Safety System

### Purpose of the Subsystem
---
The sole purpose of this system is to secure the safety of the users and the internal components of the device. The primary functions of the system come from the consumer's cabinet restrictions. Using non-contact Inductance Proximity sensors, both the consumers and inner contents of the machine shall have an extra shield from possible harm. This shall also prevent any potential damage and interference in the system’s operations.

In contrary of the original design using “RFID Coded Safety Sensors”, for budgetary reasons it was substituted for a closed loop Proximity Sensor system. As shown below, the safety system functions outside of the normal operation cycle of the machine. This allows the machine to have a “double check” in the case of tampering with one of the lock sensors. This also overrules if there are any issues with the PLC. Both the Security System sensors and Safety System sensors are required to continue operation of the device.

![image](https://user-images.githubusercontent.com/100805322/231349541-72ff11b9-4564-420f-a1ef-29ab174c4538.png)

Constraint C1 has been fulfilled by the general functionality of the proximity sensors. Since there are no doors to be sensed, the sensors have been thoroughly tested with other metallic objects.

Constraint C2 has been resolved by using a closed loop system as shown above. If this project is carried over to another team, the original system design using RDIF Safety Sensors is still viable.

Constraint C3 has been fulfilled by using relays to control the enable state of the motor driver.

---
### Constraints/Specifications
---

The design constrants are as followed:

**• The relay shall be aware of the state of each cabinet door all times. (C1)**

**• The system shall be redundant and separate from the normal operations of the PLC. (C2)**

**• The system must overrule all other functions of the system. The motor shall not have any motion while there is an error in place. (C3)**


Constraint C1 has been fulfilled by the general functionality of the proximity sensors. Since there are no doors to be sensed, the sensors have been thoroughly tested with other metallic objects.

Constraint C2 has been resolved by using a closed loop system as shown above. If this project is carried over to another team, the original system design using RDIF Safety Sensors is still viable.

Constraint C3 has been fulfilled by using relays to control the enable state of the motor driver.

---
### Experimental Procedure
---

To properly test this system, the sensors and relay system was wired and tested using in-lab power supply and DMM. The sensors were originally tested on aluminum material, and has since been experimented with other ferrous material as listed on the datasheet. After wiring the sensors and relay to match the required logic. The logic prepared resembles that of a simple AND gate, meaning all of the sensors must be activated for a signal to be sent to the motor driver. 

---
### Expected Results
---
When all the sensors detect the presence of metal, the power should flow through and enable the motor to spin. When any of the sensors don’t detect any metal, this would cut power being sent to the enable, disabling the motor.

The expected outcome is rather straightforward. The sensors will either detect the theoretical door enabling the motor, or not detect anything and disabling the motor.

---
### Collected Data
---
While the overall results of the experimentation nearly match the expected results, the process of reaching these conclusions was bumpy.

The first issue we ran into was the functionality of the motor driver’s enable.

Unlike most motor drivers, the enable for the STP-DRVAC-24025 has the negative and positive modules in parallel connected to the power supply. With the connection of the negative and ground being break in the circuit. (image for reference) 

![image](https://user-images.githubusercontent.com/100805322/231349928-ffdb728b-9291-409a-8d18-7b4590112557.png)


The final configuration is similar to the diagram shown above, with the only difference being the positive line having the break for control. So, when the Positive enable is receiving 24V of power, it ceases function.

Due to the change in the configuration for the sensors and relay, the logic being used also had to be adjusted. The AND logic described before no longer worked, and DeMorgan’s Law can into play. As shown below, the logic became NOT (A AND B) which is converted to NOT A OR NOT B.

![image](https://user-images.githubusercontent.com/100805322/231349890-56891dc2-6194-4a68-bf19-fbf86c155de0.png)

After these adjustments, the results were as expected. Whenever one of the sensors does not sense their door, the motor will cease movement and will not move until everything is in place.


https://user-images.githubusercontent.com/100805322/231724287-a65690ac-44f0-45db-8140-a93368bf456c.mp4


As shown in the video above, when the inductance sensor is within the range of a metallic object, the internal switch activates allowing current to flow through the output pin. This connection is indicated by the lights attached to the sensor. Since the metal being assessed in the video is mostly comprised of aluminum. As shown on the data sheet of the IFS240 proximity sensor, the correction factor for detecting aluminum is 0.4. The correction factor is how much the sensing range of the sensor is affected by the type of material being sensed. So, the max sensing range is reduced from 4mm to 1.6mm.

![image](https://user-images.githubusercontent.com/100805322/231723416-d378c078-7af5-4b55-a2c8-595442055ed7.png)

The material of theoretical solenoid locks would be made of stainless steel, meaning the max sensing range would be 2.8mm. The design would have the plunger of the lock well within this range.

---
### Further Improvements
---
It is suggested that the team would move forward with using the proximity sensors since the system is already in place, and the materials are already collected.
However, if possible the RFID Safety Sensors would be a vast improvement to the overall efficiency of the system. These sensors would provide greater protection and have a greater resistance to any vandalism. Another perk is the compatibility of the sensors with one another, not needing any addition components to function properly.

---
## Motor System

### Purpose of the Subsystem
---

---
### Experimental Procedure
---

---
### Expected Results
---

---
### Collected Data
---

---
### Further Improvements
---

## Secuirty and Locks System

### Purpose of the Subsystem
---

---
### Experimental Procedure
---

---
### Expected Results
---

---
### Collected Data
---

---
### Further Improvements
---

## Power Subsystem 

### Purpose of the subsystem  
---
The purpose of the subsystem is to provide the required voltage and amperage for all electrical apparatus in every subsystem (this includes the PLC, Safety Sensors, Photoelectric Sensors, Motor and Driver, and the PC), so that all of the systems of the vending machine can properly perform their functions.

The customer required the program to do a few things: store the student ID, name, email, class, and term, before ordering the machine to bring the appropriate device to the door.  

Constraint C1 requires the power system to be protect against a power surge through the use of a ground fault current interrupter. We met this constraint by powering the vending machine with a 120V power cord that has a built in GFCI; the wall outlets of Brown have built in GFCI's as well.

Constraint C2 requires the power system to convert the 120V AC voltage to what ever lower potential needed; in our case we only needed 24V. This constraint was not met exactly as that we did not have our power supply to transform the 120V into 24V, however, we were able to use the 24V power supply in the PLC lab to aquire the proper voltage we needed to supply to the PLC and Safety System.

Constraint C3 requires our power system to have an emergency stop button. This constraint is met for the GFCI power cord is connected to an exposed outlet and can easily be pulled.

---
### Experimental Procedure  
---

---
### Expected Results  
---

---
### Collected Data
---

---
### Data Interpretation
---

---
### Future Improvements
---
