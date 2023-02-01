# Security & Locks

# Subsystem Function:
This subsystem's role in our design is to secure both the stored devices and internal components of the machine. The main contributor to the security system will be the cabinet doors holding the devices. These cabinet door require digitally controlled locks, allowing access to verified users, while locking out those who would attempt to forcefully steal from the machine.


# Constraints

**• The locks must be automated and controlled by the device.**

	• Since this machinery is will be ran autonomously and unmanned, the locks must be controlled without the need of human assistance
 
**• The locks must be able to resist the forced entry of human force.**

	• The main purpose of the machine is to /contain and distribute valuable technology. 
	• Knowing that there might be attempts to break in, the locks must be strong enough to resist the average human's strength.
	
**• The cabinet doors must remain lock in the case of power outage/blackout.**

	• To prevent possible theft of inventory, the locks shall stay locked in all instances of power loss. 
	• The locks shall only be unlocked if instructed by the internal operations of the device.

![image](https://user-images.githubusercontent.com/100805322/215175968-acb86932-6f9c-450f-9555-0cdeea43c83a.png)


^Source: https://www.uxcell.com/12v-11a-114mm-electromagnetic-solenoid-lock-assembly-for-electirc-door-lock-p-1634595.html



# Analysis

## Locks
Solenoid Locks use a small electromagnet to control the plunger of the lock. When the solenoid is unpowered, the lock's plunger rest in its extended "locked" state. However, when the solenoid is powered the lock's plunger is pulled back allowing the cabinet door to be opened. This allows us to digitally control the locking state of the cabinet doors. This process is controlled by the PLC.


![image](https://user-images.githubusercontent.com/100805322/204165866-72be5f6f-c642-4785-93bd-949e7801c4d6.png)

^Source: https://electronics.stackexchange.com/questions/86443/need-a-loud-electrical-component-for-magnetic-lock


The solenoid locks will be attached to the enclosed side of the cabinet doors. There will also be protection provided to the body and wires of the locks to help prevent tampering and/or vandalism. The material of the protective shell will be determined by the mechanical team.

For the solenoid locks to be activated, they will require a voltage of 9V-12V and current 1.1 A. These charges will be controlled by the PLC, which they are directly wired to.

In the case power loss and/or blackout there is little to no loss in security, since the locks only release when the solenoid is powered.

### Solenoid Schematic
![image](https://user-images.githubusercontent.com/100805322/216149455-d948fcfc-ee5f-4a63-843c-3e4c5a2c5d9b.png)


The Schematic above shows that the **Red Wire** will be connected directly to the PLC, and the **Black Wire** to ground.


## LEDs

As a visual aid, there will LEDs next to the door present at each level. When the consumer is complete rental process, the door will pop open and the LED next to it will start blinking. While this is not a necessary function, it is a useful feature to assist the consumer.

![image](https://user-images.githubusercontent.com/100805322/216144514-e63cf09c-2e2e-4bf7-96be-157c0e7b8def.png)

^Source: https://www.amazon.com/Alpinetech-Metal-Signal-Indicator-Pilot/dp/B06XXPZBKQ/ref=asc_df_B06XXPZBKQ/?tag=hyprod-20&linkCode=df0&hvadid=309735769572&hvpos=&hvnetw=g&hvrand=6757627046684924141&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-568542064467&region_id=674469&th=1

### LEDs Schematic
![image](https://user-images.githubusercontent.com/100805322/216149557-b5c392fd-3d06-45e0-ab66-fa65d54c994e.png)


## Spring Hinges
To assist the user with identifying their cabinet door, there will be spring hinges installed. This will also help with the locks being moved away from their strike plates, keeping the door unlocked if the user was too slow to open the cabinet door.

These hinges will constantly be applying force outward to push the door open, and should be easy to close back into the locked state. While there will be slight presser on the solenoid locks, there will not be enough to do damage to them. To assure this, adjustable spring locks will be used. This will allow the alteration of spring's tension.

![image](https://user-images.githubusercontent.com/100805322/215165500-1c097ecc-c343-4317-b588-4ba76a7402d9.png)

^Source: https://www.hingeoutlet.com/products/spring-loaded-hinge-for-cabinets-304-stainless-steel-sold-individually?variant=39951404171416&msclkid=ad335ddc6f0d129234623e0dd787c6ff

As shown in the diagram above, the hinges will constantly be in the "Opening Tension Type (SO)". Constanly trying to push outwards to open the door.


# BOM
| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|11.4mm Electromagnetic Solenoid Lock| DC 12V, 1.1A | Locks | a19042500ux0016 | uxcell | 3 | $12.49 | $37.47 |
|3.5'' Self-Closing Door Hinges| Stainless Steel Adjustable 3 Pack |Locks|B08YZ2TF1F|Qkenvo| 1 | $27.99 | $27.99 |
|Signal Indicator Pilot Dash Light| 8mm 5/16" 24V AC/DC LED |Locks| PL8B-24 |Alpinetech | 3 | $5.95 | $17.85 |
| **Total** | | | | **Total Components** | 7 | **Total Cost** | $83.31 |

