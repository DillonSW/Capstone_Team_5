# Safety System (Taking a power nap dillon))

## Subsystem Function:
The sole purpose of this system is to secure the safety of both the users and the operators of the device. The primary functions of the system come from the consumer's cabinet restrictions. Using "SensaGuard"  non-contact Interlock technology, both the consumers and inner contents of the machine shall have an extra shield from possible harm.


## Constraints:

The sensors shall be aware if the "state" of the cabinet door at all times.

The system must be completely separate from the normal operations of the device.

The system must **overrule** all other functions of the system. The machine shall not continue any operations while there is an error in place.

## Subsystem 3D model

![image](https://user-images.githubusercontent.com/100805322/219275238-a8289762-a105-446a-8a5a-54a5abeedcbe.png)

## Subsystem Schematic

![image](https://user-images.githubusercontent.com/100805322/219275364-542d2202-e404-418b-a029-dc6810c77acd.png)


When an actuator moves out of the detection range, the signal from the sensors is lost alerting the PLC. While this value is reported as "low" the motor system shall lose all functionality, until the signal reports "high". The PLC will also know the state of the locks for each door. These 2 values will always be crossed referenced anytime a change is detected. If the inductive proximity sensors report the lock is in place, but the safety switch cannot sense the actuator, the system will report an error. This error must be checked and cleared by an administrator before it can return to normal functions.

# Analysis:

## Non-contact interlock switches

![image](https://user-images.githubusercontent.com/100805322/219275585-d74a4bd6-3dd5-4356-bd81-1d1f2cc7a86b.png)

^Source: https://us.idec.com/medias/safety04-03-eng.jpg?context=bWFzdGVyfHJvb3R8NDgwNTF8aW1hZ2UvanBlZ3xoMzcvaDJmLzkxNjc2NjEyMzYyNTQuanBnfDZiY2Y3NGVjMWI3ZTAwMTljOWQwNTJkOTI0OWQ1YWI1ODFiYmZjMjBjMDNiOTIzYWMyOWI5OTlmN2UyOWRjZTI

A non-contact interlock switch is a device that uses a sensor head to detect the distance between an actuator mounted to the door and a sensor head mounted to the machine and to detect information from the actuator without any direct contact between the actuator and the sensor head, and transmits the signal as door open/close information.

^Source: https://us.idec.com/idec-us/en/USD/RD/safety/guide/safety04#:~:text=A%20non-contact%20interlock%20switch%20is%20a%20device%20that,and%20transmits%20the%20signal%20as%20door%20open%2Fclose%20information.

Since the sensors are "non-contact" they will not gain much wear and tear. However, it is recommended to inspect the sensor every month for any oddities. 

**Anti-tampering Function**
There are two types of RFID type anti-tampering functions: unicode type and multi-code type. The ___ uses the Unicode method. This means that there is single specific code matched between the sensor and actuator. There is also a feature for pairing the new actuator to the sensor after purchase.

![image](https://user-images.githubusercontent.com/100805322/219281038-b7c2bbf9-96e0-44d7-8086-9a81abfa7b8b.png)

^Source: https://us.idec.com/medias/safety04-07-en.jpg?context=bWFzdGVyfHJvb3R8NDM4NzR8aW1hZ2UvanBlZ3xoOWMvaDRlLzkxMjgxMzg1MDYyNzAuanBnfDI0ZWEwNDMzZDUyZWE5MmFkNGY4YjYwZWRmNmFjYWQ3MDY2OTlhODA4MzY0MjZhZGZlZjFlNGIzOTBjYTJlZWY

## Adaptation

![image](https://user-images.githubusercontent.com/100805322/219279087-0f7633c4-b6c9-44d6-9171-55ad80ad1205.png)

As seen in the diagram above, the output cable has a total of 8-pins. Each of these pins need to be connected to seperate parts of our system to be properly utilized. Also to simplify the process, the sensors will be connected in series. By doing this if any of the sensors are missing their aucuator or are out of line, the system will report 0V to the PLC. Using Kicad a wiring model was constructed based on the sample model provided by the manufacturer. Sample seen below:

![image](https://user-images.githubusercontent.com/100805322/219280921-13addd1a-f63f-4eae-a950-8e0f9d8fa89e.png)

## Placement and Alligenment 

Each sensor will be placed on the inner side of the door frame, below the induction sensors (See Locks). The sensor component and actuator require a minimum distance of 1.97" of space betwix them.  
![image](https://user-images.githubusercontent.com/100805322/219282123-7ae174f9-8a01-4e61-8e12-526d95e35f2f.png)

^

![image](https://user-images.githubusercontent.com/100805322/219282149-cdba0efb-5ba5-4401-8828-22926a7aeb31.png)

![image](https://user-images.githubusercontent.com/100805322/219282538-918d2b68-e11e-44e6-b848-c553e211fd4e.png)


# BOM
| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|SensaGuard 440N-Z21SS2A|Non-contact switch| Safety | 440NZ21SS2A | ALLEN-BRADLEY | 3 | $155.01 | $465.03|
| **Total** |  |  |  | **Total Components** | 3 | **Total Cost** | $465.03 |
