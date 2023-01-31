# Vending Machine Subsystem - User-Interface
### Function of the Subsystem:
---
When designing vending machine the main component of the machine is to get input from the user and process that information and send that information to the rest of the parts corresponding to it. So, in the same way for ECE board vending machine the student must be able to input their information, and select products from given set of  choices so to target this requirement, UI (User Interface) subsystem is required.
 
### Specifications & Constraints:
---
 
  1. UI must not operate at greater than 100 W because of PC output rating of USB-C [1].
  2. UI must run Windows/Linux environment to run Kiosk application.
  3. Must have HDMI or type C or USB port to connect to mini-PC.
  4. UI must be at least 15" (diagonal) because of the application will be running on it & for better readability.

### Schematic:
---

<div align="center">  
  
<img src="https://user-images.githubusercontent.com/101990738/215674304-b6a2701a-473a-40c3-97a8-9fc48c575680.png" width="700" height="500" />
  
_Figure 1: Dimensions of LCD [2]_
  
<img src="https://user-images.githubusercontent.com/101990738/215674342-9ff5b894-4779-438c-9b26-2b5af4de244a.png" width="800" height="400" />
  
_Figure 2: Ports on LCD [2]_
 
<img src="https://user-images.githubusercontent.com/101990738/215674370-4b099a6e-4a77-46d6-8714-2b03312113cf.png" width="600" height="600" />
  
_Figure 3: Connections of LCD with PC [2]_

<img src="https://user-images.githubusercontent.com/101990738/215674430-0e58f4af-66ad-416c-999e-a92762f61f65.png" width="600" height="600" />
  
_Figure 4: Schematic of the System_

<div align="left"> 

### Analysis:
---
 
The vending machines' main interface with the students will be the LCD. It will be utilized for student feedback as well as for displaying information to students, such as messages about devices. Therefore, it will need to be touchscreen. There are two main types of touchscreens that are available: Resistive and Capacitive. 
 
#### 1) Resistive Touchscreen [3]
  
The fundamental components of a resistive touch screen are two substrate layers that are spaced apart by either an inert gas or air. For the top layer, a flexible film-based substrate is always used, however for the bottom layers, either film or glass may be used as the substrate. On the inner-facing surfaces of the substrate layers, opposite the air gap, a conductive substance is deposited. There are only two operational states for a resistive touch screen: touched and not touched. The conductive substance on the top layer makes electrical contact with the conducting surface of the bottom layer when a user presses down on the top surface, indenting the film in the process. This action generates a voltage differential that the system interprets as a touch. The touch controller analyzes the action after determining the precise X and Y coordinates of this contact. A resistive touch screen is like a mechanical switch as it requires physical force to operate.
  
<div align="center"> 

<img src="https://user-images.githubusercontent.com/101990738/214468780-78a23f78-cd7d-4418-8cc7-d51eb093ecf4.png" width="400" height="400" />
 
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
 
<img src="https://user-images.githubusercontent.com/101990738/214468983-1e4b5614-ddcf-46fc-92c7-82a9cec24fc7.png" width="400" height="400" />

  
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

It is evident from the finding that Capacitive touch screens outperform resistive touch displays in a variety of ways. Although more expensive, capacitive touch displays offer advantages that surpass the price, making them the better choice. Additionally, since it is used for user input it must also have sufficient screen size otherwise it will be frustrating to use that is why our team feels that 15" diagonal display measurement would be sufficient for user interaction and also the application that we will be writing to test the User Interface for the selection of different boards. Additionally, since the PC supports USB-C (Universal Serial Bus) our team has decided that a USB-C interface would work better because of two main reasons:-
 
 1. The USB Type-C port would be used to supply the LCD with the power it needs (from PC).
 
 2. Type-C offers a single interface for both power and signal. As a result, it reduces noise and avoids using two cords.
 
So to meet all the above requirements the following decision was made:

<div align="center"> 
  
|                 |    Details                                              |
|:---------------:|:-------------------------------------------------------:|
| Name/Brand      | View Sonic 15.6" Touch Screen LCD                       |
| LCD Type        | IPS (In Plane Switching Technology)                     |
| Touchscreen     | Yes (Can also be used as external monitor through HDMI) |
| Type            | Projective Capacitive                                   |
| Interface       | USB Type-C/Mini-HDMI                                    |
| Diagonal Size   | 15.6"                                                   |
| Consumption     | 8.6 W (Typical)        10.5 W (Max)                     |
| Documentation   | Good                                                    |

<div align="left">
  
### BOM (Bill of Materials): 
---
  
<div align="center">
 
|      Part             |    Price             |
|:---------------------:|:--------------------:|
| ViewSonic LCD         | $ 269.99             |
| USB-C to USB-C cable  | (-) Included         |
| USB-C to USB-A cable  | (-) Included         |
| Mini-HDMI cable       | (-) Included         |
| Passive Touch Pen     | (-) Included         | 
| **Total**             | **$269.99**           |
 
<div align="left">
  
**Link to the product:**   
  
[1] https://www.bestbuy.com/site/viewsonic-15-6-lcd-fhd-monitor-displayport-vga-usb-hdmi/6428015.p?skuId=6428015&ref=NS&loc=101
 
[2] https://www.viewsonic.com/us/td1655-15-6-portable-1080p-ips-touch-monitor-with-60w-usb-c-and-mini-hdmi.html

 
### References: 
---
[1]. https://manhattanproducts.eu/pages/usb-c-pd-charging-everything-you-need-to-know
  
[2]. https://www.viewsonic.com/us/td1655-15-6-portable-1080p-ips-touch-monitor-with-60w-usb-c-and-mini-hdmi.html
 
[3]. https://forum.digikey.com/t/resistive-touch-vs-capacitive-touch-whats-the-difference/1063
  
[4]. https://www.researchgate.net/publication/356667592_Fabrication_and_Performance_Evolution_of_AgNP_Interdigitated_Electrode_Touch_Sensor_for_Automotive_Infotainment
  

  


