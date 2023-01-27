# Security & Locks

# Subsystem Function:
This subsystem's role in our design is to secure both the stored devices and internal components of the machine. The main contributor to the security system will be the cabinet doors holding the devices. These cabinet door require digitally controlled locks, allowing access to verified users, while locking out those who would attempt to forcefully steal from the machine.


# Constraints

**• The locks must be automated and controlled by the device.**
 
**• The locks must be able to resist the forced entry of human force.**

**• The "state" of the locks must be known at all times.**
	
**• The cabinet doors must remain lock in the case of power outage/blackout.**

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
![image](https://user-images.githubusercontent.com/100805322/215167025-d333aa8e-a9c4-4979-93f6-acc4f8bfc8fe.png)

The Schematic above shows that the **Red Wire** will be connected directly to the PLC, and the **Black Wire** to ground.

## Proximity Sensors
As both a safety precaution and security measure, there needs to be a confirmation of the door being closed and the lock being locked.

![image](https://user-images.githubusercontent.com/100805322/214712598-c768a960-efea-4fbe-93c7-c0bce5f58a88.png)

^Source: https://files.pepperl-fuchs.com/selector_files/navi/productInfo/pds/085298_eng.pdf

To confirm the state of the locking mechanism, there will be an inductive proximity sensor installed on each level. An inductive proximity sensor only detects the presence of metallic objects, making it difficult for tampering. This proximity version of the sensor has a detection range of 4mm, allowing room for error for contact. This also prevents damage being done to the sensors every time the plunger enters the strike plate. 

For the proximity sensors they will also be directly connected to the  PLC. Their connection will remained closed as long as they are in proximity of the lock plunger. The will open their connection with the PLC every time the plunger of the lock is missing from the strike plate.

The proximity sensors will be installed into the sides of the opening of the cabinet doors. They will be directly aligned with the solenoid locks.

### Sensor Schematic
![image](https://user-images.githubusercontent.com/100805322/215167070-507815db-264e-4fce-a3e6-fe238a426a55.png)

The Schematic above show that **Wire 1** will be connected to ground, **Wrie 2** will be connected to the power source, and **Wire 3** will connected to the output pins of the PLC.

This type of senosr is known as PNP, meaning when it is activated it produces a high signal and outputs it to the PLC, signifying the presence of the lock.

## Spring Hinges
To assist the user with identifying their cabinet door, there will be spring hinges installed. This will also help with the locks being moved away form their strikeplates, keeping the door unlocked if the user was too slow to open the cabinet door.

These hinges will constantly be applying force outward to push the door open, and should be easy to close back into the locked state. While there will be slight pressser on the solenoid locks, there will not be enough to do damage to them. To assure this, adjustable spring locks will be used. This will allow the alteration of spring's tension.

![image](https://user-images.githubusercontent.com/100805322/215165500-1c097ecc-c343-4317-b588-4ba76a7402d9.png)

^Source: https://www.hingeoutlet.com/products/spring-loaded-hinge-for-cabinets-304-stainless-steel-sold-individually?variant=39951404171416&msclkid=ad335ddc6f0d129234623e0dd787c6ff

As shown in the diagram above, the hinges will constantly be in the "Opening Tension Type (SO)". Constanly trying to push outwards to open the door.


# BOM
| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|11.4mm Electromagnetic Solenoid Lock| DC 12V, 1.1A | Locks | a19042500ux0016 | uxcell | 3 | $12.49 | $37.47 |
|Proximity Inductive Sensor| PNP Normally Open Two-wire| Lock Sensors |NBN4-12GM60-WS-V12 | PEPPERL & FUCHS | 3 | Provided by school | N/A |
|3.5'' Self-Closing Door Hinges| Stainless Steel Adjustable 3 Pack |Locks|B08YZ2TF1F|Qkenvo| 1 | $27.99 | $27.99 |
| **Total** | | | | **Total Components** | 5 | **Total Cost** | $65.46 |

