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

