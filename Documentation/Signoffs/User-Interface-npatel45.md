Vending Machine Subsystem - User-Interface
-----

#### Function of the Subsystem:
When designing vending machine the main component of the machine is to get input from the user and process that information and send that information to the rest of the parts corresponding to it. So, in the same way for ECE board vending machine the student must be able to input their information, and select products from given set of  choices so target this requirement, UI (User Interface) subsystem is required.
  
•	Receive information from student using medium of a touch screen LCD (Liquid Crystal Display)
 
#### Specifications & Constraints:
 
  1. Must be able to recognize depression of any keys and relay that information to mini-PC
  2. Must be able to send or display instructions coming from or to mini-PC
  3. Must be able to establish a direct connection with mini-PC
  4. Must be big and bright enough to read it from
  5. Must have HDMI or type C or USB port to connect to mini-PC
 
For the User Interface subsystem to function properly, LCD touch screen would need to display messages/signals coming from different subsystems or sometimes even from Interface itself. For example, if a student tries to access a particular option from the menu the touch screen must be able to send that information to mini-PC and in return display the information received back from mini-PC to let the user know whether the selected task was successfully completed or was not, and if not it should also display the reason so that it can help student understand what he/she did wrong (1,2,3). Additionally, the monitor should be big enough so that the student won't have to squint their eyes and bend down to see what is on the display prompt (4).
 
#### Schematic:

<p align="center">
  <img width="200" height="500"src="https://user-images.githubusercontent.com/101990738/203384791-31476dac-30a9-4180-b971-6cc2a40c4488.png">
</p>

 
 
 
 
 
 
 
 
 
 





 
Analysis:
 
The vending machines' main interface with the pupils will be the LCD. It will be utilized for student feedback as well as for displaying information to students, such as messages about whether the board has been successfully checked out or not. Therefore, it will need to be touchscreen. There are two main types of touchscreens that are available: Resistive and Capacitive. The following points were made for each one:
Resistive 	 	Capacitive	 
Pros	Cons	Pros 	Cons
 	 	 	 
Low Cost	Unable to react to multiple-touch sensing	Durability	expensive compared to resistive touchscreen
Less possibility of accidental contact	Less sensitive, and as a result, requires pressure to function.	Facilitates Customization	Because it is highly sensitive, even the slightest touch can cause it to activate, which could result in inadvertent contact.
Can detect any object when properly pressured.	Lower display clarity is caused by a thick top layer.	Offers functions for multiple-touch sensing.	 
Higher sensor resolution	The screen is more vulnerable to scuffing and scratches.	Easy to Clean	 
 	Expensive to fix	 	 
 	If the screen has a minor fracture, it won't function.	 	 
 	 	 	 
 
 It is evident from the above table that capacitive touch screens outperform resistive touch displays in a variety of ways. Although more expensive, capacitive touch displays offer advantages that surpass the price, making them the better choice. Additionally, since it is used for user input it must also have sufficient screen size otherwise it will be frustrating to use that is why our team feels that 7" diagonal display measurement would be sufficient for user interaction. Also, since the mini-PC supports USB (Universal Serial Bus) interface our team has decided that a USB interface would be better because of two main reasons:
i.	The USB port would be used to supply the LCD with the power it needs (from Mini-PC)
ii.	USB offers a single interface for both cord and signal. As a result, it reduces noise and avoids using two cords.
 
So to meet all the requirement the following finding was made:
 
LCD	Elecrow 7" Touch Screen LCD
LCD Type	TFT (Thin-film-transistor liquid-crystal display)
Touchscreen	Capacitive
Interface	USB/HDMI
Diagonal Size	7"
Driving Voltage	 5V@1A
Documentation 	Mediocre
 
BOM: 
********************

