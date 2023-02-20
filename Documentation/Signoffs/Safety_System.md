# Safety System

## Subsystem Function:
The sole purpose of this system is to secure the safety of both the users and the operators of the device. The primary functions of the system come from the consumer's cabinet restrictions. Using "SensaGuard" non-contact Interlock technology, both the consumers and inner contents of the machine shall have an extra shield from possible harm. This shall also protect the integrty of the vending device's processes, it can be considered a type of oversheilding for the devices functions.


## Constraints:

**• The sensors shall be aware if the "state" of each cabinet door at all times. (C1)**

**• The system shall be redundant and separate from the normal operations of the PLC. (C2)**

**• The system must overrule all other functions of the system. The machine shall not continue any operations while there is an error in place. (C3)**

*Reset button must be pressed


## Subsystem 3D model

![image](https://user-images.githubusercontent.com/100805322/219275238-a8289762-a105-446a-8a5a-54a5abeedcbe.png)

## Subsystem Schematic

![image](https://user-images.githubusercontent.com/100805322/220061514-7c38ad18-dd22-42c4-b2b8-a78aaa7d3078.png)

## System Design:

  At the frame of each door there will be a safety sensor and it's paired actuator. These sensors are then wired in series and connected to a Safety Relay to be monitored.

  When an actuator moves out of the detection range, the signal from the sensors is lost alerting the relay. While this value is reported as "low" the motor system shall lose all functionality, until the reset button is pressed.  **(C3)**

# Analysis:

### Safety Relay

![image](https://user-images.githubusercontent.com/100805322/220069237-251fcc47-ca8b-4f98-9b06-cf5fd7e19ec3.png)

  A safety relay is a relay made specificly to monitor the safety of a machine. The safety relay will be connected to the non-contact interlock switches, and will report when any switch is missing the signal of their actuator. In the case the system's motor starts while the safey report is going off, it will trigger an immediate shut down of the system's functions.
  
  The hardware chosen for the device meets the standards required by ISO 13849-1 (Safety of Machinery) and IEC 61508/IEC 62061 (Functional Safety of Electronic Safety-related Systems), and meet all the specifications of our system.

  In conjunction with the safety relay will be a manual RESET switch. It was decided that it would be better to have a manual switch in place of an automated variant. While there are sensors that can confirm if the doors where closed, there is no absolute way to know if the space is clear of any objects. Also, if the relay ever forces a system shutdown, it will need to be inpected by an administrator. It will be inspected for any hardware issuse and possible tamperage. 

  After the all clear is given, the administrator will unlock the interal machine lock and press the RESET switch. 

### Non-contact interlock switches (C1)

After doing some research, it was found that using Non-contact interlock switches would work best for the vending device. Using RFID technology, these sensors have several layers of protection and are considered to be the **"Gold Standard"** for RFID coded safey sensors.

    Note: The "Gold Standard" phase is sourced from Professor Jesse Roberts of Tennessee Technological University

![image](https://user-images.githubusercontent.com/100805322/219275585-d74a4bd6-3dd5-4356-bd81-1d1f2cc7a86b.png)

^Source: https://us.idec.com/medias/safety04-03-eng.jpg?context=bWFzdGVyfHJvb3R8NDgwNTF8aW1hZ2UvanBlZ3xoMzcvaDJmLzkxNjc2NjEyMzYyNTQuanBnfDZiY2Y3NGVjMWI3ZTAwMTljOWQwNTJkOTI0OWQ1YWI1ODFiYmZjMjBjMDNiOTIzYWMyOWI5OTlmN2UyOWRjZTI


> A non-contact interlock switch is a device that uses a sensor head to detect the distance between an actuator mounted to the door and a sensor head mounted to the machine and to detect information from the actuator without any direct contact between the actuator and the sensor head, and transmits the signal as door open/close information.

^Source: https://us.idec.com/idec-us/en/USD/RD/safety/guide/safety04#:~:text=A%20non-contact%20interlock%20switch%20is%20a%20device%20that,and%20transmits%20the%20signal%20as%20door%20open%2Fclose%20information.


    Note: Since the sensors are "non-contact" they will not gain much wear and tear. 
    However, it is recommended to inspect the sensor every month for any oddities. 

### Anti-tampering Function (C2)

There are two types of RFID type anti-tampering functions: Unicode type and Multi-code type. The SensaGuard uses the Unicode method. This means that there is single specific code matched between the sensor and actuator. There is also a feature for pairing the new actuator to the sensor after purchase.

![image](https://user-images.githubusercontent.com/100805322/219281038-b7c2bbf9-96e0-44d7-8086-9a81abfa7b8b.png)

^Source: https://us.idec.com/medias/safety04-07-en.jpg?context=bWFzdGVyfHJvb3R8NDM4NzR8aW1hZ2UvanBlZ3xoOWMvaDRlLzkxMjgxMzg1MDYyNzAuanBnfDI0ZWEwNDMzZDUyZWE5MmFkNGY4YjYwZWRmNmFjYWQ3MDY2OTlhODA4MzY0MjZhZGZlZjFlNGIzOTBjYTJlZWY

And as stated in the System Design, the state of the safety sensors will be cross referenced with the induction sensors. The induction sensors are a part of the normal system functions, while the safety sensors act as a monitor of the door. The induction sensors can be tampered with nearly any piece of metal, meaning the safety sensor's coded RFID is the real line of defense. **(C2)**

### Adaptation

![image](https://user-images.githubusercontent.com/100805322/219279087-0f7633c4-b6c9-44d6-9171-55ad80ad1205.png)

*^Tabel 2*

As seen in the diagram above, the output cable has a total of 8-pins. Each of these pins need to be connected to separate parts of our system to be properly utilized. Also, to simplify the process the sensors will be connected in series. By doing this if any of the sensors are missing their actuator or are out of line, the system will report 0V to the Safety Relay. Using Kicad a wiring model was constructed based on the sample model provided by the manufacturer. Sample seen below:

![image](https://user-images.githubusercontent.com/100805322/219280921-13addd1a-f63f-4eae-a950-8e0f9d8fa89e.png)

*^Figure 5*

## Placement and Alignment 

Each sensor will be placed on the inner side of the door frame, below the induction sensors (See [Locks System](https://github.com/DillonSW/Capstone_Team_5/blob/main/Documentation/Signoffs/Security_Locks.md)). The component's dimensions are reflected in the 3D mock up below. (Values in inches)

![image](https://user-images.githubusercontent.com/100805322/219282123-7ae174f9-8a01-4e61-8e12-526d95e35f2f.png)

![image](https://user-images.githubusercontent.com/100805322/219282149-cdba0efb-5ba5-4401-8828-22926a7aeb31.png)


The sensor component and actuator require a minimum distance of 1.97" of space betwix them. This is shown in *Figure 3* from the user manual on the manufacturer's website.

![image](https://user-images.githubusercontent.com/100805322/219317607-ba010073-7c85-412f-9d6a-a4de02f399b3.png)

*^Figure 3*

These conditions are reflected in the mock up 3D model shown below. (Full model at top of page)

![image](https://user-images.githubusercontent.com/100805322/219282538-918d2b68-e11e-44e6-b848-c553e211fd4e.png)

    Note: It should also be noted that only the sensor piece of the pair requires a wired connection. 
    This means the actuator doesn't require any extra components or wiring attached to the door.
**Table 2, Figure 5, and Figure 3 are from the *SensaGuard Rectangular Flat Pack Installation Instructions* found [here](https://www.rockwellautomation.com/en-us/products/hardware/allen-bradley/safety-products/safety-sensors/safety-interlock-switches/non-contact-interlock-switches/440n-sensaguard.html)**

# BOM
| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|SensaGuard 440N-Z21SS2A|Non-contact switch| Safety | 440NZ21SS2A | ALLEN-BRADLEY | 3 | $155.01 | $465.03|
| **Total** |  |  |  | **Total Components** | 3 | **Total Cost** | $465.03 |
