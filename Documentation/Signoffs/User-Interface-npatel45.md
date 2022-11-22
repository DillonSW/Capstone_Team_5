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

<div align="center"> 
  
![image](https://user-images.githubusercontent.com/101990738/203420602-62791559-bc8c-4834-87f6-5370614b598a.png)
  
<div align="left"> 

#### Analysis:
 
The vending machines' main interface with the pupils will be the LCD. It will be utilized for student feedback as well as for displaying information to students, such as messages about whether the board has been successfully checked out or not. Therefore, it will need to be touchscreen. There are two main types of touchscreens that are available: Resistive and Capacitive. The following points were made for each one:
 
 ##### Resistive Touchscreens
 - Pros
    - Low Cost
    - Less possibility of accidental contact
    - Can detect any object when properly pressure
    - Expensive compared to resistive touchscreen
    - Higher sensor resolution
- Cons
    - Unable to react to multiple-touch sensing
    - Less sensitive, and as a result, requires pressure to function.
    - Lower display clarity is caused by a thick top layer.
    - The screen is more vulnerable to scuffing and scratches.
    - Expensive to fix
    - If the screen has a minor fracture, it won't function.
 
 ##### Capacitive Touchscreens
 - Pros
    - Durability
    - Facilitates Customization
    - Offers functions for multiple-touch sensing.
    - Easy to Clean
 - Cons
    - Expensive compared to resistive touchscreen
    - Because it is highly sensitive, even the slightest touch can cause it to activate, which could result in inadvertent contact.

It is evident from the finding that **Capacitive touch screens** outperform resistive touch displays in a variety of ways. Although more expensive, capacitive touch displays offer advantages that surpass the price, making them the better choice. Additionally, since it is used for user input it must also have sufficient screen size otherwise it will be frustrating to use that is why our team feels that 7" diagonal display measurement would be sufficient for user interaction. Also, since the mini-PC supports USB (Universal Serial Bus) interface our team has decided that a USB interface would be better because of two main reasons:-

   1. The USB port would be used to supply the LCD with the power it needs (from Mini-PC)
   1. USB offers a single interface for both cord and signal. As a result, it reduces noise and avoids using two cords.
 
So to meet all the above requirements the following decision was made:

<div align="center"> 
  
|                 |    Details                                              |
|:---------------:|:-------------------------------------------------------:|
| Name/Brand      | Elecrow 7" Touch Screen LCD                             |
| Touchscreen     | Yes (Can also be used as external monitor through HDMI) |
| Type            | Capacitive                                              |
| Interface       | USB/HDMI                                                |
| Diagonal Size   | 7"                                                      |
| Driving Voltage | 5V @ 1A                                                 |
| Documentation   | Mediocre                                                |

<div align="left">
  
#### BOM (Bill of Materials): 
  
<div align="center">
 
|                 |    Details                                              |
|:---------------:|:-------------------------------------------------------:|
| Name/Brand      | Elecrow 7" Touch Screen LCD                             |
| Touchscreen     | Yes (Can also be used as external monitor through HDMI) |
| Type            | Capacitive                                              |
| Interface       | USB/HDMI                                                |
| Diagonal Size   | 7"                                                      |
| Driving Voltage | 5V @ 1A                                                 |
| Documentation   | Mediocre                                                |
  
<div align="left">
  


