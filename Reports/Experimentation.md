# Experimental Analysis  
 
## Identification Subsystem 

### Purpose of the subsystem  
---
The purpose of the subsystem is to store student information into a database and automatically assign the student the correct board depending on class selection. The system has not met all of the original constraints due to issues obtaining the part orders. It is important to note that the original specifications have been met in another way.  

The customer required the program to do a few things: store the student ID, name, email, class, and term, before ordering the machine to bring the appropriate device to the door.  

Most of the constraints enumerated in the signoff have not been met due to original desires because parts never arriving for the team, however, the constraints have been partially satisfied by substituting the needed hardware with software.  

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

Picture ?

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
