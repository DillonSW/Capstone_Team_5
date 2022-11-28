# Security & Locks

# Subsystem Function:
This subsystem's role in our design is to secure both the stored devices and internal components of the machine. The main contributor to the security system will be the cabinet doors holding the devices. These cabinet door require digitally controlled locks, allowing access to verified users, while locking out those who would attempt to forcefully steal from the machine.


# Constraints

**• The locks must be controlled digitally.**
 
**• The locks must be able to resist the forced entry of human force.**

**• The "state" of the locks must be known at all times.**
	
**• The labinet doors must remain lock in the case of power outage/blackout.**

![image](https://user-images.githubusercontent.com/100805322/204165855-432babae-403e-43d8-9ac5-47d1b4751871.png)

^Source: https://www.uxcell.com/12v-11a-114mm-electromagnetic-solenoid-lock-assembly-for-electirc-door-lock-p-1634595.html



# Analysis

### Locks
Solenoid Locks use a small electromagnet to control the plunger of the lock. When the solenoid is unpowered, the lock's plunger rest in its extended "locked" state. However, when the solenoid is powered the lock's plunger is pulled back allowing the cabinet door to be opened. This allows us to digitally control the locking state of the cabinet doors. This process is controlled by the PLC.


![image](https://user-images.githubusercontent.com/100805322/204165866-72be5f6f-c642-4785-93bd-949e7801c4d6.png)

^Source: https://electronics.stackexchange.com/questions/86443/need-a-loud-electrical-component-for-magnetic-lock


The solenoid locks will be attached to the enclosed side of the cabinet doors. There will also be protection provided to the body and wires of the locks to help prevent tampering and/or vandalism. The material of the protective shell will be determined by the mechanical team.

For the solenoid locks to be activated, they will require a voltage of 9V-12V and current 1.1 A. These charges will be controlled by the PLC, which they are directly wired to.

In the case power loss and/or blackout there is little to no loss in security, since the locks only release when the solenoid is powered. 

### Proximity Sensors
As both a safety precaution and security measure, there needs to be a confirmation of the door being closed and the lock being locked.

To confirm the state of the locking mechanism, there will be an inductive proximity sensor installed on each level. An inductive proximity sensor only detects the presence of metallic objects, making it difficult for tampering. This proximity version of the sensor has a detection range of 4mm, allowing room for error for contact. This also prevents damage being done to the sensors every time the plunger enters the strike plate. 

For the proximity sensors they will also be directly connected to the  PLC. Their connection will remained closed as long as they are in proximity of the lock plunger. The will open their connection with the PLC every time the plunger of the lock is missing from the strike plate.

The proximity sensors will be installed into the sides of the opening of the cabinet doors. They will be directly aligned with the solenoid locks.




# BOM
| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|11.4mm Electromagnetic Solenoid Lock| DC 12V, 1.1A | Locks | a19042500ux0016 | uxcell | 3 | $12.49 | $37.47 |
|Proximity Sensor Switch SN04-N| 3Pcs 4mm 3-Wire 6V-36V |Locks| SN04-N |RATTMMOTOR | 1 | $13.00 | $13.00 |
| **Total** | | | | **Total Components** | 4 | **Total Cost** | $50.47 |

