# Sensors System 

  

## Subsystem Function  

  

The role of the sensor subsystem is to send signals—communicating the status of the device occupancy of the presently forefront compartment sections on all three dial layers—to the PLC to update certain tags, so that the PLC's ladder logic code can properly use that information ad hoc.   

  

 

## Constraints  

  

**The Sensor System:** 

   

* **1. Cannot take up more than eight input pins from the PLC**    

   ^The Siemens PLC module S7-1200 has fourteen input pins of which six have already been designated to inputs from other systems.

 

* **2. The distance sensor chosen must determine the presence or absence of a device by measuring whether the light emitted was reflected back from a distance range of 3.75 to 7.25 inches** 

   ^The minimum distance a device will be from the sensor is 3.75 inches, and the maximum distance a device will be positioned from the sensor is 7.25 inches.

   ^The sensor must not sense up more than a distance of 11.25 inches; this is the length of the compartment and the closest the sensor will be to the dial. This is to     prevent mistakenly sensing the back wall of the compartment as a device. 

 

* **3. Must send a one signal to the PLC if there is a device in the presently forefront compartment section and a zero signal if there is not.**  

   ^This constraint is chosen when considering the consequences in the case of the wire being cut: 

If the default (zero) signal communicates that a device is present then the door could be able to be opened, upon someone trying to check a device out, because         the PLC thinks there is a device there to be distributed. 

If the default (zero) signal communicates that a device is not present then the door will remain locked and cannot be unlocked because the PLC thinks there is no       device there to distribute. 

Upon reflection the second option is the best because the devices are protected behind the locked door which will prevent theft during the time period before the       wire connection is fixed. 

 

* **4. The sensor must be mounted in the space of 3.75in. by 6in. by 0.75in that is between the door and compartment**

   ^The area floor space between the door and the compartment is 3.75x6.00 inches
   ^The height from the floor space to the bottom of the door is 0.75 inches
 

  

## Schematic  

![SensorSchemTwo](https://user-images.githubusercontent.com/113734069/217380138-199f1886-35f7-4af5-aea6-7a4fc8a7bff7.jpg)

![SensorCloseUp](https://user-images.githubusercontent.com/113734069/217380154-e397efea-276e-494a-b7a1-fea440842e03.jpg)

Each sensor possesses three wires; the power and neutral wires are connected to the power system, and the signal wires are connected to the PLC system.

![SensorPosition1](https://user-images.githubusercontent.com/113734069/218870843-fcd08064-6d51-4506-af23-63962e144b81.jpg)

![SensorPosition2](https://user-images.githubusercontent.com/113734069/218870858-45943f5f-0281-4a83-9ad9-a2d2db802dc2.jpg)

![SensorPosition3](https://user-images.githubusercontent.com/113734069/218870866-d7e30379-019d-4b73-88fb-587186a5a512.jpg)

![SensorPosition4](https://user-images.githubusercontent.com/113734069/218870874-adb4fdab-5fa9-480b-91c2-0637fe34debb.jpg)

![SensorPosition5](https://user-images.githubusercontent.com/113734069/218870885-55f4b90c-7245-4fc8-96c1-b1d0db8a5283.jpg)

The sensor has two thredded holes to mount onto the floor using screws right below the door with the emitter and receiver elements pointing towards the door. The sensor can be moved up to three inches closer to the compartment if needed to satisfy the distance range constraint.



## Analysis  

**Constraint 1 - Input Pins**

Using three ifm spot sensors with one bit signals will only take up three I/O pins on our PLC, which is less than the maximum of eight allowed.


**Constraint 2 - Distance Sensing Range**

Our chosen sensor measures up to a range of 0.60 inches to 7.87 inches; this will cover the 7.25 inch maximum distance requirement; this will also cover the 3.75 inch minimum distance requirement.
The sensor is not capable of sensing the back wall because it is 11.50 inches from the beginning of the compartment which is out of the sensors range.
The background suppression of the sensor also could be used to not sense the back wall.


**Constraint 3 - Signaling**

Our chosen sensor has negative and positive switching on the output signal, therefore the sensor is capacble of sending a positive output signal if it senses an object and a negative output signal if it does not sense an object.

The sensor can be connected electrically to the power and PLC systems through the ifm OGH580 connector cord.


**Constraint 4 - Sufficient Space and Mounting**

The length of the sensor, 2.07 inches, suffices the 6.0 inch maximum.
The width of the sensor, 1.40 inches, suffices the 3.75 inch maximum.
The height of the sensor, 0.75 inches, suffices the 0.75 inch maximum.

The OGH580 has two threaded holes to screw the sensor into the floor plate to mount.
  
  

## BOM  

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| OGH580 | Diffuse Reflection sensor with background suppression | Sensors | OGH-FPKG/US/CUBE  | ifm Efector inc. | 3 | $109.00 | $327.00 |
| EVC001 | Female Cord set | Sensors | ADOGH040MSS0002H04 | ifm Efector inc | 3 | $11.50 | $34.50 |
| **Total** |  |  |  | **Total Components** | 6 | **Total Cost** | $361.50 |
