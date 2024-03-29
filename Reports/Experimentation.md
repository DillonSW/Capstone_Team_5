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
To test this subsystem, a user entered data through the GUI and it was verified to be inside of the database on the host with the correct assigned board. The inventory entered in the program was also verified to be inside the database. The running of the motor will be demonstrated in the PLC analysis, and the Error checking will be shown in the GUI analysis. The communication via OPC was verified as shown in the below video by sending and receiving signals to and from the tag. 

---
### Expected Results  
---
The team expected the student data to be in the database in alphabetical order along with the rented board determined by the step count handled by the program. The inventory was also expected to be present with its rented and stored date because a student cannot rent without a device in the machine.
A total of 10 random students were entered into the database along with 15 random devices. We also expected the motor to turn correctly based on the values sent to the PLC. 

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

![SpecsPC](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/CapstonePC_Specs.png)  

As you can see in the photo above, the CPU is stronger than an Intel Core i5 and the Memory is 16 GB.

Below you can see the results of running the database program while taking input from the GUI. The database needed to hold all 10 test entries in the student database and keep track of the rented device and student information. 

![Students_Results](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/Students_Results.png)  

Below you can see the results of the inventory table after testing the entry of 15 devices and the renting of 10. The devices should be removed in order of entry into the machine.  

![Inventory_Results](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/Inventory_Results.png)

---
### Data Interpretation
---
For C1, you can see in the third figure that the boxnumbers were correctly taken in by the database along with the rented and stored dates. This is the result the team expected to see when entering through the database.  

Constraint C4 is satisfied by allowing the user to enter his or her ID into the GUI. As you can see the data entered in figure 2 is all present in the database as expected.  

Given that the PC has a Core i7 and 16GB of RAM, the comupter specs are decent enough to run the PLC application needed for programming. This satisfies constraint C7 and C9 in the list.   

In figure 2, the student data was entered and stored in the correct format. All required information from our customer is provided through the GUI and stored after error checking procedures.  

In figure 3, the device information was stored correctly after being entered by an administrator. Students are not allowed to decide the board received and therefore the device location is also stored in the database. 

---
### Measures of Success
---
The measure of success for the ID system states that the program must correctly store the boxnumbers and student information. For the OPC communication, the program needed to send and receive signals to and from the database. In the following video it can be shown that the OPC communication correctly activated the motor, and the previous results show the data from the GUI being stored correctly into MySQL. 

Video : https://youtu.be/tVvsogPO3sM

---
### Future Improvements
---
Several improvements can be made on this system because parts need to be installed in a future version, and the database can be expanded. The next team that receives the project must make sure to install the barcode scanner and card reader to the machine. The card reader is needed because, as of now, the student can enter any correctly formatted T#. The system should take information from the card so a student cannot fake information. The voltmeter must also be acquired to monitor the operation of the barcode and card scanners.  

## GUI Subsystem

### Purpose of the subsystem
---
The purpose of the graphic user insterface is to take information from the user and store it into the database through the ID subsystem. The interface allows for a convenient way to rent a device for a class and provides error checking to verify information is in the correct format.

The interface is able to let a user input information into the ID subsystem and provide the student with notifications while renting a device. The GUI must follow certain constraints determined during the design of the project. The team was not able to order a touchscreen for the project, but received a ubuntu 20.04 computer from the school IT department instead. 

---
### Constraints/Specifications
---

  1. UI must run Windows/Linux environment to run the application.
  2. Must have HDMI or type C or USB port to connect to PC.
  3. UI must be at least 15.6" (diagonal) because of the TIA (Totally Integrated Automation) Portal application.
  4. UI must be anchored to prevent theft problems.

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

Below is the all the data that was collected for input validation for different fields if a student were to mistype some of the input fields or if they were to skip some fields and hit the submit button directly.

| | | 
|:--------------------:|:--------------------:|
![Delete](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/Admin_Delete.png) Figure 1: Admin_Delete| ![Agree](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/Agreement_Error.png) Figure 2: Agreement_Error| 
![Email](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/Email_Error.png) Figure 3: Email_Error| ![Field](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/Field_Error.png) Figure 4: Field_Error|
![ID_Error](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/ID_Error.png) Figure 5: ID_Error| ![Load_Complete](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/Load_Complete.png) Figure 6: Load_Complete| 
![Load_Mode](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/Load_Mode.png) Figure 7: Load_Mode| ![Name_Error](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/Name_Error.png) Figure 8: Name_Error| 

---
### Data Interpretation
---

For C2, we can clearly see that the computer provided by IT departmnent was able to run the GUI written using python in Linux Environment. Also, we can see that different errors were generated for different input fields in the pictures listed above.

If needed to delete the database by an associate then the command that is set to do so is "delete" in ID field and "admin" in name field. This keywords can be changed anytime as per the needs of associate, and if did so correctly then the figure 1 depicts what it would return and will delete the information stored in database.

For the load mode, the keyword to enter the number of boards is "load" in ID field and "admin" in name field. If did correctly, it would open a prompt where an associate would type in the boards manually. This was done as a substitute because of the barrring ordering issues and parts not arriving on time. The boards loaded propertly in the database can be seen in ID subsystem (figure 3).

For different input fields, different errors can be seen as shown in table above.If a student were to input the email address incorrectly, then the popup shown in figure 3 would let the student know that they are typing the email wrong. If the name entered by the student in the name field doesn't have first and last name then the program would throw an error to them saying they need to type the first and last name as shown in figure 8. If for some reason, a student forgot to type the T in the ID field then the program would tell the user that they need to enter "T" before the ID as seen in figure 5. If a student were to skip one of the input fields and agree to the terms and conditions and try to submit the information then figure 4 shows that it would throw an error message asking the user to fill all input fields.

At last, if the student filled all the information, but failed to agree to the terms and conditions and tried to submit the information then the program wouldn't let it do so and ask the user to select and go over it as shown in figure 2. All these validations are also protected against SQL injection as each entry field is looking for specific keyword. For example, ID has to start with "T", name field is looking for only two words i.e. First and Last Name, for email the entered username has to end with Techs domain of tntech.edu, and at last the drop down menus are read only so the students don't have any way to inject queries and extract information of students.

To protect students from accidentally closing the program we implemented a special keybinding so that students don't close it intentionally or unintentionally and access the student information. To do so, the program is set to close with the keybinding of "Alt + Z" as our team thinks that this combination wouldn't be used that frequently.This keybinding can be changed like other commands by associates if needed.

---
### Measures of Success
---
The measure of success for the GUI system states that the program must be easy to use and also must prevent SQL injection by throwing errors when inforamtion is incorrectly entered. The following video shows the layout of the GUI which is also shown above, and the video also shows errors being thrown when information was incorrectly entered. 

Video : https://youtu.be/tVvsogPO3sM

---
### Future Improvements
---
Several improvements can be done to this subsystem. In future, if the IT department allows to order the Touchscreen UI as originally proposed then that can be used for GUI as that would get rid off extra hardware. Also, another improvement would be making the GUI more intuitive so students or associates could navigate it easily, also  if the future capstone team were to get SD card for PLC then they could integrate the PLC with the program so that they both can perform synchronously, and at last the machine is made up to hold one board but in case if they students were to expand the design so that the machine can hold multiple boards then some modifications would have to be done for GUI with some additonal details.

## PLC System

### Purpose of the Subsystem
---
The purpose of the PLC system is to be the middle-man between our database and our physical peripherals such as the motor and LEDs. The reason we chose to use a PLC in addition to a Linux PC is because PLCs are designed to handle physical control faster and more efficiently than a PC.

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
Constraints C1 and C2 required us to have the memory card for our PLC, which does satisfy these constraints. But, due to ordering issues, we are using the PLCs in our PLC lab, which have 8 digital input and outputs. So, with what we have, C1 is satisfied. However Constraint C2 is no longer within the scope of this project due to us swtiching to a PLC with 8 digital inputs and outputs.

Constraint C3 is satisfied, even with the ordering issues. The PLC setup that we are using is 24-inches long, and less than 6-inches deep and tall. So, our system will fit within a 3x1x1 foot area, and C3 is satisfied.

Constaint C4 is satisfied with the PLC we are using. The PLCs in the lab have two 48V fuses, one that is rated for 2A and the other for 4A. This satisfies IEC-61131-2(6.4.4.3) for protection from physical damage.

Constraint C5 is satisfied by the use of a custom OPC client that can read-from and write-to the PLC.

https://user-images.githubusercontent.com/100802994/231836664-d108fc11-3d49-4a41-928a-dcc6a42da2b6.mov

Above is a video recording of us using the OPC client to control the PLC, which is controlling the motor driver.

![OPC](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Software/PLC_OPC.jpeg)

The image above is of the OPC client running on our Linux VM. The client first reads the value of the controller tag, then changes it to "true" or "energized" and reads it again. This along with the video show that the OPC is able to communicate with the PLC.  

---
## Data Interpretation
---
The video collected above shows how constraint C5 was satisfied through our OPC client. When the client is ran, it energizes a controller tag associated with stepping the motor. As will be shown (as best as we can) in the motor system analysis section, we did not touch the PLC code in our Studio 5000 software. Instead we had a stopwatch up on the screen to time how long it took the motor to complete a full rotation.

---
### Measures of Success
---
The measure of success for the PLC system states that the program must correctly control the peripherals given signals from the OPC. In the following video, it can be seen that the motor correctly activates and turns after being given the signal from the OPC. The other peripherals have not been connected because the parts were never received. 

Video : https://youtu.be/Vv9zIDt42ac

---
### Further Improvements
---
The main point that can be said about future improvements is ordering the peripherals and writing the code to control them. Another improvement that could be made is to the pulsing sequence for stepping. Currently it is two TON timers that read the .DN boolean of the other timer. There is a way to make a rising-edge detection sequence using only one timer, but I do not rememeber how. If this was implemented, the code would look cleaner and allow for more efficient pulse width modulation.

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

To properly test this system, the sensors and relay system was wired and tested using in-lab power supply and DMM. The sensors were originally tested on aluminum material, and has since been experimented with other ferrous material as listed on the datasheet. After wiring the sensors and relay to match the required logic. The logic prepared resembles that of a simple AND gate, meaning all of the sensors must be activated for a signal to be sent to the motor driver. When the enable recieves a positive input, the motor stops all movement.

---
### Expected Results
---
When all the sensors detect the presence of metal, the power should flow through and enable the motor to spin. When any of the sensors don’t detect any metal, this would cut power being sent to the enable, disabling the motor and ceasing all movement.

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


https://user-images.githubusercontent.com/100805322/234241463-0bac8268-ea57-4a61-8167-c97eb8001625.mp4

As shown in the video above, the safety sensors are functioning properly and are working in conjunction to the motor system. Every time either of the sensors aren't in range of the piece of metal, the motor will completely stop. While only 2 sensors are presented in the video, the process can be simply replicated up to 8 times. The relay module being used has the capability to logically control 8 inputs/outputs. Simply repeating the logic discussed earlier allows for more controlling inputs and it all leads to the same output.


https://user-images.githubusercontent.com/100805322/231724287-a65690ac-44f0-45db-8140-a93368bf456c.mp4


As shown in the video above, when the inductance sensor is within the range of a metallic object, the internal switch activates allowing current to flow through the output pin. This connection is indicated by the lights attached to the sensor. Since the metal being assessed in the video is mostly comprised of aluminum. As shown on the data sheet of the IFS240 proximity sensor, the correction factor for detecting aluminum is 0.4. The correction factor is how much the sensing range of the sensor is affected by the type of material being sensed. So, the max sensing range is reduced from 4mm to 1.6mm.

![image](https://user-images.githubusercontent.com/100805322/231723416-d378c078-7af5-4b55-a2c8-595442055ed7.png)

The material of theoretical solenoid locks would be made of stainless steel, meaning the max sensing range would be 2.8mm. The design would have the plunger of the lock well within this range.

---
### Measures of Success
---
The measure of success for the safety system states that the sensors must interrupt the motor's enable signal while also being seperated from the PLC. This assures that all movement of the motor will cease, securing the safety of the device and possible deviants. In the video below, it can be shown that the sensors properly interrupt the motor and do not allow it to turn when the sensors were removed. 

Video : https://youtu.be/iVfy9IWk9oA

---
### Further Improvements
---
It is suggested that the team would move forward with using the proximity sensors since the system is already in place, and the materials are already collected.
However, if possible the RFID Safety Sensors would be a vast improvement to the overall efficiency of the system. These sensors would provide greater protection and have a greater resistance to any vandalism. Another perk is the compatibility of the sensors with one another, not needing any addition components to function properly.

---
## Motor System

### Purpose of the Subsystem
---
The purpose of the motor system is to rotate the platforms holding the boards for check out. It was decided that the motor should be a hybrid stepper motor due to their high precision and accuracy, as well as having high torque. This motor system is controlled by the PLC communicating with the motor driver; the driver will send pulses to the motor's phases (A+/-, B+/-) to make it step. Because the motor can operate at many different resolutions (or steps per revolution), we chose to do full-stepping or 1.8 degrees per step. This is because we planned to have 20 boards on each platform, meaning there are 18 degrees between each board. If we full-step the motor, we can reach the next board in 10 steps.

---
### Specifications/Constraints
---
The list of constraints on specifically the **MOTOR** are listed below. In the Motor System signoff, there are many constraints listed before the motor is even mentioned. This is because there had to be concrete information and constraining of the platform material and the boards to best decide which motor we needed to use. (Weight, strength, dimensions, quantity, etc). Some of these constraints were also given to the mechanical team so they could use them as constraints on the framework.

C1: The motor shall be able to rotate a mass weighing a total of 70.858 lbs. Assuming roughly 20% tolerance for error, it must be able to rotate 85 lbs.

C2: The motor shall be protected at 125% of the nameplate current rating, or be protected at 3.19A.

C3: The motor system shall follow the NEC 310-16 Table for wiring.

---
### Experimental Procedure
---
Constraint C1 cannot feasibly be measured, as we did not have a way to safely place 85 lbs on the motor's shaft. Constraint C2 is also not feasibly measurable. The multimeters that we have access to cannot fit in the grommet holes on our enclosure. Because we have hot 120VAC in the enclosure when powered, we must keep the enclosure shut for safety.

However, we can run a test to see if the motor can truly reach 200 steps/revolution. Our PLC has a count-up accumulator that counts to 200 and stops the motor once it is reached.

---
### Expected Results
---
The expected results of this procedure are the motor being able to complete a full rotation in 200 steps and in a reasonable time. This was done with the aid of recording software and also slowing down the motor to a speed so that one could reliably count the steps. If 200 steps is truly a full rotation, then 10 steps would make the motor rotate 18 degrees, which is how far we want. Assuming there is at least 1 minute between two students checking out a board, the motor must be able to step 10 times in 1 minute, or 200 times in 20 minutes.

---
### Collected Data
---

We cannot safely test the current that is going into the motor. Our enclosure's grommet holes are not large enough to fit a DMM's prongs, and the driver (and motor leads) must be enclosed whenever we are powering the driver.

Constraint C2 is no longer within the scope of this project as we did not receive the fuse breakers required to protect the driver. **But** the motor driver can sense overcurrent and shut everything off if that threshold is reached.

Constraint C3 is satisfied due to the motor and driver being consumer-rated, so their wire gauges have been properly chosen by the manufacturer.

![MotorSpeed](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Images/Tables/Motor_Speed_Average.jpg)

The table above shows the 30 tests we ran on the motor to see if it could rotate 200 steps (or one rotation) within a reasonable time. The average for one rotation was aroudn 20 seconds, meaning in order to rotate 10 steps, the motor would need 1 second. This is more than reasonable for motor speed, which we thought the stepper motor could easily reach.

Video of Collected Data: https://youtu.be/f2e1zKOUCzw

**Note**: The video above is the same as the PLC System video. 

---
### Measures of Success
---
The measure of success for the Motor system states the machine should turn within several seconds to a board. Given that it takes on average 20 seconds to fully rotate, the time to the next slot is 1 second.  

---
### Further Improvements
---
A future improvement could be finding a way to safely measure the current going to the motor. It may be difficult since almost all of the motor system's wirings are within the 120VAC enclosure that **must** be closed when powered. Another improvement could be finding a way to actually place 85 lbs worth of material on the motor shaft to measure torque. Maybe it can be done once the mechanical housing is complete.

## Security and Locks System

### Purpose of the Subsystem
---
This subsystem's role in our design is to secure both the stored devices and internal components of the machine. The main contributor to the security system will be the cabinet doors holding the devices. These cabinet doors require digitally controlled locks, allowing access to verified users, while locking out those who would attempt to forcefully steal from the machine.

---
### Constraints/Specifications
---

**• The locks shall respond to the commands of the PLC. (CL-1)**
	
**• The locks shall remain extended when power is lost. (CL-2)**

**• The inductance sensors shall inform controlling PLC of lock status at all times. (CP-1)**

**• There shall be visual indicators to inform the user of the location of their device. (CI-1)**

**• The door shall open as soon as locks are released, preventing the door re-locking before device is removed. (CS-1)**

**• The locks shall resist the force of resisting spring force of internal spring hinges. (CS-2)**
	
**• Unauthorized users of the device shall not be able to access internal content. (CD-1)**


Constraints for the Locks (CL-1, CL-2), LEDs (CI-1), Spring Hinges (CS-1, CS-2), and Doors (CD-1) are now considered out of the scope of this project. Due to ordering issues, these parts were not received and therefore cannot be implemented.

The only Constraint still in scope is CP-1, which states “The inductance sensors shall inform controlling PLC of lock status at all times.”

---
### Experimental Procedure
---

#### Inductance Sensors
Since these sensors are also implemented in the Safety System, their experimental process is practically identical. The sensors and relay systems were wired and tested using in-lab power supply and DMM. The sensors were originally tested on aluminum material, and has since been experimented with other ferrous material as listed on the datasheet.

#### Solenoid Locks
To properly test the solenoid locks, their connection and responsiveness to commands from the PLC would be examined. While these locks have rated voltage and current draw, they would still be tested for their accuracy and efficiency.

#### Spring Hinges
Since the selected hinges have adjustable springs, they would be tested for the outward force and stiffness. The Optimal value would allow the door to open without external assistance, but also loose enough for the user to close it back. They would also be tested with the resistant force value of the solenoid locks, as they are the force holding the doors shut.

#### LEDs
The LEDs would be tested for their responsiveness and longevity. They would also need to be tested with the PLC, assuring they're compatible and can be controlled.

---
### Expected Results
---

It is assumed that the components would function properly and be compatible with one another.

---
### Collected Data
---
The only data that could be collected was that of the inductance proximity sensors, which discussed in depth in the Safety System.

The data from the other components cannot be collected since they are not in our possession.

---
### Measures of Success
---
The Lock system could not be measured without the approriate parts.  

---
### Further Improvements
---
As the system is currently designed, it should be fully functional and meet the listed constraints. However, this is only in theory and needs to be tested further for confirmation of functionality. Once the components are collected, they should be tested and put to use.


## Power Subsystem 

### Purpose of the subsystem  
---
The purpose of the subsystem is to provide the required voltage and amperage for all electrical apparatus in every subsystem (this includes the PLC, Safety Sensors, Photoelectric Sensors, Motor and Driver, and the PC), so that all of the systems of the vending machine can properly perform their functions.

---
### Constraints/Specifications
---

Constraint C1 requires the power system to be protect against a power surge through the use of a ground fault current interrupter. We met this constraint by powering the vending machine with a 120V power cord that has a built in GFCI; the wall outlets of Brown have built in GFCI's as well.

Constraint C2 requires the power system to convert the 120V AC voltage to what ever lower potential needed; in our case we only needed 24V. This constraint was not met exactly as that we did not have our power supply to transform the 120V into 24V, however, we were able to use the 24V power supply in the PLC lab to aquire the proper voltage and current we needed to supply to the PLC and Safety System.

Constraint C3 requires our power system to have an emergency stop button. This constraint is met for the GFCI power cord is connected to an exposed outlet and can easily be pulled.

---
### Experimental Procedure  
---
In order to meet constraint C3 we tested whether the power system was supplying current but not to much current, we measured the current drawn by the PLC and safety system inductance sensors with a multimeter. 

---
### Expected Results  
---
We expected the Inductance sensor to have a current below the maximum current draw of 200mA.

We expected the PLC to have a current below the maximum current draw of 1500mA.

---
### Collected Data
---
The safety system inductance sensors has varying a current draw between 6.5 and 7.0 mA.
![SafetyCurrentDrawPlot](https://user-images.githubusercontent.com/113734069/231815847-94ed3ced-dea6-435d-9fa7-bb249657869a.png)

The PLC has a varying current draw between 9.5 and 9.7 mA
![PLCCurrentDrawPlot](https://user-images.githubusercontent.com/113734069/231815879-9e4665be-1966-4872-80d1-52187643fe99.png)

---
### Data Interpretation
---
The current Amperage data that we aquired fell far short from our maximum set current draws.
Both systems combined would draw at most 16.7mA.
With a maximum allowed current draw of 4000mA (otherwise our circuit breaker would open the circuit), there is no worry of too much power draw by our PLC and Safety systems.

Constraint C1 was satisfied by the use of a GFCI cord for the motor driver enclosure.  

Constraint C2 is no longer within the scope of this version due to unforseen circumstances with ordering. 

---
### Measures of Success
---
The measure of success for the Power system states that the rest of the systems should be powered from this system. Due to ordering issues, the measurement could not be verified. 

---
### Future Improvements
---
In the next version of the machine, the missing parts that could not be received need to be ordered and can be installed according to the signoff. The entire din rail must be constructed and the blocks must be installed along with circuit breakers. 


## Sensor Subsystem 

### Purpose of the subsystem  
---
The role of the sensor subsystem is to send signals—communicating the status of the device occupancy of the presently forefront compartment sections on all three dial layers—to the PLC to update certain tags, so that the PLC's ladder logic code can properly use that information ad hoc.

---
### Constraints/Specifications
---
Constraint C1 requires the sensor system to not take up more than eight input pins from the PLC. This constraint is easily met as only three pins are used by all of the sensors combined.

Constraint C2 requires that the distance sensor chosen must determine the presence or absence of a device by measuring whether the light emitted was reflected back from a distance range of 3.75 to 7.25 inches. This constraint also requires that the sensor does not sense more than up to 11.25in so as not to sense the back side of the compartment.

Constraint C3 requires the sensors to send a one signal to the PLC if there is a device in the presently forefront compartment section and a zero signal if there is not.

---
### Experimental Procedure  
---
 To test for C2 and C3, we would calibrate the sensor to sense up to its max range and use a voltmeter to determine whether the sensor sends a signal or not at varying distances between 1 and 12 inches.

---
### Expected Results  
---
We expect to read a voltage between the sensors range of 0.60 inches to 7.87 inches which covers the max distance of 7.25in that must be covered.
We would expect the sensor to not sense past 8in which means the back wall would not be picked up by the sensor.
We would expect to read a voltage when the sensor sees and object and not see a voltage when it does not see and object within its range.

---
### Collected Data
---
No data could be collected due to never receiving the parts to this system. 

---
### Data Interpretation
---
Since no data could be collected, there is no interpretation of the data. 

---
### Measures of Success
---
The measure of success for the Sensor system states that the sensors should test the state of the door. Due to ordering issues, the measurement could not be verified. 

---
### Future Improvements
---
In the next version of the machine, the missing parts that could not be received need to be ordered and can be installed according to the signoff. These parts must than be wired up and calibrated to meet desired specifications.
