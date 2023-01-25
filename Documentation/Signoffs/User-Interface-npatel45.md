# Vending Machine Subsystem - User-Interface
### Function of the Subsystem:
---
When designing vending machine the main component of the machine is to get input from the user and process that information and send that information to the rest of the parts corresponding to it. So, in the same way for ECE board vending machine the student must be able to input their information, and select products from given set of  choices so to target this requirement, UI (User Interface) subsystem is required.
 
### Specifications & Constraints:
---
 
  1. UI must not operate at greater than 5 V 0.5 A because of mini-PC output rating [1].
  2. UI must run Windows/Linux environment to run Kiosk application.
  3. Must have HDMI or type C or USB port to connect to mini-PC.
 
### Schematic:
---

<div align="center">  
  
![image](https://user-images.githubusercontent.com/101990738/203437345-1d371ec5-7c23-4b43-86b6-ec64e5d2023c.png)
  
_Figure 1: Dimensions of LCD [2]_
  
![image](https://user-images.githubusercontent.com/101990738/203420602-62791559-bc8c-4834-87f6-5370614b598a.png)
  
_Figure 2: Ports on LCD [2]_

![image](https://user-images.githubusercontent.com/101990738/203436487-dcc3a30c-626c-4406-9c1c-32b90ba2831c.png)
  
_Figure 3: Connections of LCD with mini-PC [2]_
  
 ![image](https://user-images.githubusercontent.com/101990738/214427528-1e055347-bf93-408f-95fb-df147eb98fa9.png)
  
_Figure 4: Schematic of the System_

<div align="left"> 

### Analysis:
---
 
The vending machines' main interface with the students will be the LCD. It will be utilized for student feedback as well as for displaying information to students, such as messages about whether the board has been successfully checked out or not. Therefore, it will need to be touchscreen. There are two main types of touchscreens that are available: Resistive and Capacitive. 
 
#### 1) Resistive Touchscreen [3]
  
The fundamental components of a resistive touch screen are two substrate layers that are spaced apart by either an inert gas or air. For the top layer, a flexible film-based substrate is always used, however for the bottom layers, either film or glass may be used as the substrate. On the inner-facing surfaces of the substrate layers, opposite the air gap, a conductive substance is deposited. There are only two operational states for a resistive touch screen: touched and not touched. The conductive substance on the top layer makes electrical contact with the conducting surface of the bottom layer when a user presses down on the top surface, indenting the film in the process. This action generates a voltage differential that the system interprets as a touch. The touch controller analyzes the action after determining the precise X and Y coordinates of this contact. A resistive touch screen is like a mechanical switch as it requires physical force to operate.
  
<div align="center"> 
 
![image](https://user-images.githubusercontent.com/101990738/214468780-78a23f78-cd7d-4418-8cc7-d51eb093ecf4.png)
  
 _Figure 5: Working of Resistive Touchscreen [4]_
  
 <div align="left"> 
   
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

#### 2) Capacitive Touchscreen [3]
  
The base of capacitive touch panels is a collection of conductors that generate an electromagnetic field. The user's conductive finger or object pulls or adds charge to the capacitive field, adjusting its strength, as they touch the screen. Based on the sort of input it receives, a touch controller measures the position of this change and then orders the system to do a certain action. Users only need to tap a capacitive touch screen for a device to recognize their input. Contrary to resistive touch displays, there is no need for physical pressure. Capacitive touch screens can support a variety of inputs, with varied motions and additional contact points instructing the system to execute a variety of actions, which is another important distinction from resistive touch technology.
     
<div align="center"> 
  
![image](https://user-images.githubusercontent.com/101990738/214468983-1e4b5614-ddcf-46fc-92c7-82a9cec24fc7.png)
  
 _Figure 6: Working of Capacitive Touchscreen [4]_
  
 <div align="left"> 
  
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
  
### BOM (Bill of Materials): 
---
  
<div align="center">
 
|      Part         |    Price             |
|:-----------------:|:--------------------:|
| Elecrow LCD       | $ 63.99              |
| USB cable         | (-) Included         |
| HDMI cable        | (-) Included         |
| **Total**         | **$63.99**           |
 
<div align="left">
  
**Link to the product:**   
  
[1] https://www.amazon.com/ELECROW-Display-1024X600-Function-Raspberry/dp/B01GDMDFZA/ref=asc_df_B01GDMDFZA/?tag=&linkCode=df0&hvadid=309779531175&hvpos=&hvnetw=g&hvrand=10466085907421531413&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9013670&hvtargid=pla-442095369518&ref=&adgrpid=62412137260&th=1
  
[2] https://www.elecrow.com/7-inch-1024-600-hdmi-lcd-display-with-touch-screen.html
  


### References: 
---
[1]. https://resources.pcb.cadence.com/blog/2020-what-are-the-maximum-power-output-and-data-transfer-rates-for-the-usb-standards
  
[2]. https://www.elecrow.com/7-inch-1024-600-hdmi-lcd-display-with-touch-screen.html
 
[3]. https://forum.digikey.com/t/resistive-touch-vs-capacitive-touch-whats-the-difference/1063
  
[4]. https://www.researchgate.net/publication/356667592_Fabrication_and_Performance_Evolution_of_AgNP_Interdigitated_Electrode_Touch_Sensor_for_Automotive_Infotainment
  

  


