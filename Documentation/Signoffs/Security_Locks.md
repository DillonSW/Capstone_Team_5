# Security & Locks

# Subsystem Function:
This subsystem's role in our design is to secure both the stored devices and internal components of the machine. The main contributor to the security system will be the cabinet doors holding the devices. These cabinet door require digitally controlled locks, allowing access to verified users, while locking out those who would attempt to forcefully steal from the machine.


# Constraints

**• The locks shall respond to the commands of the PLC. (CL-1)**
	
**• The locks shall remain extended when power is lost. (CL-2)**

	• To prevent possible theft of inventory, the locks shall stay locked in all instances of power loss. 
	• The locks shall only be unlocked if instructed by the internal operations of the device.

**• The inductace sensors shall inform controlling PLC of lock status at all times. (CP-1)**

**• There shall be visual indicators to inform the user of the location of their device. (CI-1)**

**• The door shall open as soon as locks are released, preventing the door re-locking before device is removed. (CS-1)**

**• The locks shall resist the force of resisting spring force of internal spring hinges. (CS-2)**

	• The main purpose of the machine is to /contain and distribute valuable technology. 
	• Knowing that there might be attempts to break in, the locks must be strong enough to resist the average human's strength.
	
**• Unauthorized users of the device shall not be able to access internal contents. (CD-1)**



##Full Schematic

![image](https://user-images.githubusercontent.com/100805322/218368938-986fe195-542e-4137-b127-5ed3081dfaa3.png)


## System 3D Model

![image](https://user-images.githubusercontent.com/100805322/217455449-d2c761a1-c7b3-4a8a-8719-1d96ef04a43b.png)


![image](https://user-images.githubusercontent.com/100805322/216899967-c88bcf9e-e61c-4b12-bbfe-7d03c8625cf0.png)


Shown above is the current design of one of the cabinet doors. The front of the machine will have 3 cabinet doors, one on each level of the rotating platforms. They act as the sole consumer accesspoint and protect the contents of the cabinet. Each door comes with a solenoid lock, inductance sensor, and an adjustable hinge.

When a costumer completes the rental process, the solenoid lock will release and the spring-loaded hinge will push the door open. This allows the user to take the contents of the cabinet, their newly registered device. The user would then push the door close, returning the door back to it's original state. This confirmed by inductance sensors placed at the strike plate of every lock. (Note: The machine can **NOT** continue any operation until the door is closed. For more see the [Safety System](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-signoff-Safety-System/Documentation/Signoffs/Safety_System.md).)

# Analysis

## Locks

![image](https://user-images.githubusercontent.com/100805322/215175968-acb86932-6f9c-450f-9555-0cdeea43c83a.png)

^Source: https://www.uxcell.com/12v-11a-114mm-electromagnetic-solenoid-lock-assembly-for-electirc-door-lock-p-1634595.html

Solenoid Locks use a small electromagnet to control the plunger of the lock. When the solenoid is unpowered, the lock's plunger rest in its extended "locked" state. However, when the solenoid is powered the lock's plunger is pulled back allowing the cabinet door to be opened. This allows us to digitally control the locking state of the cabinet doors. This process is controlled by the PLC. 


![image](https://user-images.githubusercontent.com/100805322/204165866-72be5f6f-c642-4785-93bd-949e7801c4d6.png)

^Source: https://electronics.stackexchange.com/questions/86443/need-a-loud-electrical-component-for-magnetic-lock


The solenoid locks will be attached to the enclosed side of the cabinet doors. There will also be protection provided to the body and wires of the locks to help prevent tampering and/or vandalism. The material of the protective shell will be determined by the mechanical team.

For the solenoid locks to be activated, they will require a voltage of 9V-12V and current 1.1 A. These charges will be controlled by the PLC, which they are directly wired to. (CL-1)

In the case power loss and/or blackout there is little to no loss in security, since the locks only release when the solenoid is powered. (CL-2)

### Solenoid Schematic
![image](https://user-images.githubusercontent.com/100805322/218368857-1675542a-b42b-44d6-b9cf-dbe1bee05eec.png)


The Schematic above shows that the **Red Wire** will be connected directly to the PLC, and the **Black Wire** to ground.

## Proximity Sensors
As both a safety precaution and security measure, there needs to be a confirmation of the door being closed and the lock being locked.

![image](https://user-images.githubusercontent.com/100805322/216234552-8831e31a-b840-447b-9390-d6f44b8ad6f9.png)


^Source: https://files.pepperl-fuchs.com/selector_files/navi/productInfo/pds/085298_eng.pdf


To confirm the state of the locking mechanism, there will be an inductive proximity sensor installed on each level. An inductive proximity sensor only detects the presence of metallic objects, making it difficult for tampering. This proximity version of the sensor has a detection range of 4mm, allowing room for error for contact. This also prevents damage being done to the sensors every time the plunger enters the strike plate.

The proximity sensors they will also be directly connected to the PLC. Their connection will remain open as long as they are in proximity of the lock plunger. They will close their connection with the PLC every time the plunger of the lock is missing from the strike plate. (CP-1)

The proximity sensors will be installed into the sides of the opening of the cabinet doors. They will be directly aligned with the solenoid locks.

### Sensor Schematic

![image](https://user-images.githubusercontent.com/100805322/218368799-1d76e5bc-c8cc-488c-b84b-9144e9306788.png)



## LEDs

As a visual aid, there will LEDs next to the door present at each level. When the consumer is complete rental process, the door will pop open and the LED next to it will start blinking. While this is not a necessary function, it is a useful feature to assist the consumer. (CI-1)

![image](https://user-images.githubusercontent.com/100805322/216144514-e63cf09c-2e2e-4bf7-96be-157c0e7b8def.png)

^Source: https://www.amazon.com/Alpinetech-Metal-Signal-Indicator-Pilot/dp/B06XXPZBKQ/ref=asc_df_B06XXPZBKQ/?tag=hyprod-20&linkCode=df0&hvadid=309735769572&hvpos=&hvnetw=g&hvrand=6757627046684924141&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-568542064467&region_id=674469&th=1

After the door has been confirmed to be closed, the LED will turn off and return to standby mode.

### LEDs Schematic
![image](https://user-images.githubusercontent.com/100805322/216149557-b5c392fd-3d06-45e0-ab66-fa65d54c994e.png)


## Spring Hinges
To assist the user with identifying their cabinet door, there will be spring hinges installed. This will also help with the locks being moved away from their strike plates, keeping the door unlocked if the user was too slow to open the cabinet door. (CS-1)

These hinges will constantly be applying force outward to push the door open, and should be easy to close back into the locked state. While there will be slight presser on the solenoid locks, there will not be enough to do damage to them. To assure this, adjustable spring locks will be used. This will allow the alteration of spring's tension. (CS-2)

![image](https://user-images.githubusercontent.com/100805322/215165500-1c097ecc-c343-4317-b588-4ba76a7402d9.png)

^Source: https://www.hingeoutlet.com/products/spring-loaded-hinge-for-cabinets-304-stainless-steel-sold-individually?variant=39951404171416&msclkid=ad335ddc6f0d129234623e0dd787c6ff

As shown in the diagram above, the hinges will constantly be in the "Opening Tension Type (SO)". Constanly trying to push outwards to open the door.

## Door's Design

The current design of the doors are shown below.

![image](https://user-images.githubusercontent.com/100805322/217455449-d2c761a1-c7b3-4a8a-8719-1d96ef04a43b.png)

Each door shall have mounting for a solenoid lock and a SensaGuard actuator (See [Safety System](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-signoff-Safety-System/Documentation/Signoffs/Safety_System.md))

Since there will be spring hinges installed on each door, the risk of handles can be eliminated. This will prevent possible vandalist from using brute force to pry open the cabinet doors. (CD-1)


# BOM
| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|11.4mm Electromagnetic Solenoid Lock| DC 12V, 1.1A | Locks | a19042500ux0016 | uxcell | 3 | $12.49 | $37.47 |
|Proximity Inductive Sensor| PNP Normally Open Two-wire| Safety |NBN4-12GM60-WS-V12 | PEPPERL & FUCHS | 3 | Provided by school | N/A |
|3.5'' Self-Closing Door Hinges| Stainless Steel Adjustable 3 Pack |Locks|B08YZ2TF1F|Qkenvo| 1 | $27.99 | $27.99 |
|Signal Indicator Pilot Dash Light| 8mm 5/16" 24V AC/DC LED |Locks| PL8B-24 |Alpinetech | 3 | $5.95 | $17.85 |
| **Total** | | | | **Total Components** | 10 | **Total Cost** | $83.31 |

