#Safety System

#Subsystem Function:
The sole purpose of this system is to secure the safety of both the users and the operators of the device. The primary functions of the system come from cabinet restrictions, modified chassis, and informational stickers. Another focus of this system is to meet all the requirement of having a piece of electrical machinery. These standards are mostly taken from OSHA's Electrical General Requirements page.



#Constraints:

• The system must protect users from possible self-harm
		○ While it can be assumed that no one would put themselves in harm's way, there must still be precautions put in place. As engineers we must follow Murphy's Law and prepare for possible shortcomings.

• The system must overrule all other functions of the device
		○ To further emphasize the importance of the user's safety, this system will need to have priority over all other "front panel" functions. Using the term front panel to describe all functions that are accessible and not those concerned with internal computing.

• The device should meet all of the General Requirements found in standard 1926.403 of OSHA
		○ 1926.403(a) States that All electrical conductors and equipment shall be approved.
		○ 1926.403(b)(1) States that the all of the equipment should be examined and should meet the following conditions:
			i. Suitability for installation and use in conformity with the provisions of this subpart. Suitability of equipment for an identified purpose may be evidenced by listing, labeling, or certification for that identified purpose.
			ii. Mechanical strength and durability, including, for parts designed to enclose and protect other equipment, the adequacy of the protection thus provided.
			iii. Electrical insulation.
			iv. Heating effects under conditions of use.
			v. Arcing effects.
			vi. Classification by type, size, voltage, current capacity, specific use.
			vii. Other factors which contribute to the practical safeguarding of employees using or likely to come in contact with the equipment.
		○ 1926.403(b)(2) Listed, labeled, or certified equipment shall be installed and used in accordance with instructions included in the listing, labeling, or certification.
		○ 1926.403(c): Equipment intended to break current shall have an interrupting rating at system voltage sufficient for the current that must be interrupted.
		○ 1926.403(d)(1): Electric equipment shall be firmly secured to the surface on which it is mounted.
		○ 1926.403(d)(2): Cooling. Electrical equipment which depends upon the natural circulation of air and convection principles for cooling of exposed surfaces shall be installed so that room air flow over such surfaces is not prevented by walls or by adjacent installed equipment.
		○ 1926.403(g): Electrical equipment shall not be used unless the manufacturer's name, trademark, or other descriptive marking by which the organization responsible for the product may be identified is placed on the equipment and unless other markings are provided giving voltage, current, wattage, or other ratings as necessary.
		○ 1926.403(h): Each service, feeder, and branch circuit, at its disconnecting means or overcurrent device, shall be legibly marked to indicate its purpose, unless located and arranged so the purpose is evident.
		○ 1926.403(i)(1): Sufficient access and working space shall be provided and maintained about all electric equipment to permit ready and safe operation and maintenance of such equipment.

#Analysis

##Proximity Sensors
As both a safety precaution and security measure, there needs to be a confirmation of the door being closed and the lock being locked.

![image](https://user-images.githubusercontent.com/100805322/216234552-8831e31a-b840-447b-9390-d6f44b8ad6f9.png)


^Source: https://files.pepperl-fuchs.com/selector_files/navi/productInfo/pds/085298_eng.pdf


To confirm the state of the locking mechanism, there will be an inductive proximity sensor installed on each level. An inductive proximity sensor only detects the presence of metallic objects, making it difficult for tampering. This proximity version of the sensor has a detection range of 4mm, allowing room for error for contact. This also prevents damage being done to the sensors every time the plunger enters the strike plate.
The proximity sensors they will also be directly connected to the PLC. Their connection will remain open as long as they are in proximity of the lock plunger. They will close their connection with the PLC every time the plunger of the lock is missing from the strike plate.

Since the sole use of these sensors is for the user's safety, the reported state of these sensors will override all other functions of the device. This primarily focuses on the Motor, since it will lose all function when the proximity sensor reports any oddities. 
The proximity sensors will be installed into the sides of the opening of the cabinet doors. They will be directly aligned with the solenoid locks.

###Sensor Schematic

![image](https://user-images.githubusercontent.com/100805322/216234644-d1355bb9-bc2b-4a79-9722-932f4204abf6.png)


Airflow 

1926.403(d)(2): Cooling.


To keep the enclosed electronics from overheating, there will be a ventilation system installed. To have the proper amount of air flow blowing through the machine, CFM had to be found. 

CFM or its elaboration “cubic feet per minute” is referred to as the amount of air that can be moved per cubic foot in a minute. Also referred to as “airflow”. When a fan is set to its maximum speed, the CFM is calculated by utilizing both the volume of air and the rate at which the fan blades move.
From <https://topcoolingfan.com/what-is-cfm-and-how-to-calculate-cfm/> 
	
To find the CFM you need the total volume of the machine is multiplied by how often the air would need to be swapped out over the course of an hour (ACH:). Since CFM is Cubic Feet per Minute, divide the value by 60 to find the CFM.
	
	
Based on the current 3D model we have on solid works, there is a total of 4386.27 cubic inches or 2.538 cubic feet
	by replacing the air every minute, a minimum of 2.538 CFM would be required. However, since we are housing electronics, the more air we can have flow through over the course of an hour the better. So changing out the air in the machine 10 times every minute would be 25.38 CFM.
	
The Wathai EC Axial fan provides the system with an airflow of 43.6 ±10%CFM which meets the standards calculated for the current version of the device.
	![image](https://user-images.githubusercontent.com/100805322/216234953-0901f74b-743e-48c5-933b-4244a14dd532.png)

	
	
Fan Schematic

![image](https://user-images.githubusercontent.com/100805322/216234984-543bb107-9850-457c-a734-a0b89fc0692d.png)

	
Fan 3D Model Representation

![image](https://user-images.githubusercontent.com/100805322/216235024-a6837c10-03a4-4dff-b4e3-3374d2794f7a.png)
	


BOM
| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|Brushless Cooling Fan| 120V AC Axial Fan | Safety | B07SDDSCY1 | Wathai | 2 | $14.99 | $29.98 |
|Proximity Inductive Sensor| PNP Normally Open Two-wire| Safety |NBN4-12GM60-WS-V12 | PEPPERL & FUCHS | 3 | Provided by school | N/A |
| **Total** |  |  |  | **Total Components** | 4 | **Total Cost** | $29.98 |
