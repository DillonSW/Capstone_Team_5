# Safety System (WIP)

Subsystem Function:
The sole purpose of this system is to secure the safety of both the users and the operators of the device. The primary functions of the system come from cabinet restrictions. Using RFID technology, the state of the cabinet door shall be reported anytime the machine wishes to continue operation.

Constraints:

Sensors:
Shall be powered by:

Shall be ran in parallel to the main operating system, not in tandem.

Shall be ran every checkout cycle

Scanner shall only recognize the presence of assigned RFID tags, all running at 13.56MHz

Shall meet the standards listed in ISO 14443A (Range less than 10 cm) (Operating Frequency 13.56MHz)

Tags:
Shall be compatible with selected sensors


Controller:
Shall meet all requirements of selected RFID sensors.

Shall receive digital input from PLC

Shall output signal to PLC



![image](https://user-images.githubusercontent.com/100805322/217458056-5c594a7e-693d-4731-baea-a1db60da5011.png)


System Design:

Each door will have an RFID configuration comprising of an RFID chip and it's parried sensor. The chip is attached to the roof of the door and the sensor is attached to the top of the door frame, both out of sight. Instead of a constant scan like the inductance sensor (See Lock System), these will be activated during the safety check. Every time the lock sensor confirms the door is closed (i.e. the lock is locked), a safety check is ran to see is all the RFID chips can be sensed. If any of the chips are missing during the check, the system goes into "restricted mode". The machine will need to be inspected by a system administrator and reset for the system to continue functions.

The sensors will be ran using a Arduino ATMega. This code will be ran every time the system is alerted to start.

The RFID chips each have a unique id that is assigned to be read by each sensor.


Analysis

![image](https://user-images.githubusercontent.com/100805322/217458089-41d77e88-9e2f-43ff-8086-64d8a8be8eee.png)


^Source: RC522 RFID Module Pinout, Features, Specs & How to Use It (components101.com)


All required specs can be found in the seller's product description and on developer's datasheet.

The RFID sensors selected are low powered and is easy to control. The MFRC522 is a highly integrated read/write chip that runs at the required 13.56MHz and has a limited range of 5cm max (3cm tested). These values fall within the range required of the ISO 14443 standards for Type A cards.

The MFRC522 also supports non-contact, two-way data transmission rate up to 848kbit/s.

Operating current :13-26mA/DC 3.3V


The Elegoo MEGA2560 R3 requires a 5V input voltage (7-12V input voltage max)
Allows the usage of a single I/O pin for operation

If any chip is missing or out of place, the MEGA shall return a low signal to the PLC

Amazon.com: HiLetgo 3pcs RFID Kit - Mifare RC522 RF IC Card Sensor Module + S50 Blank Card + Key Ring for Arduino Raspberry Pi : Electronics


# BOM
| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|RFID Kit|RC522 RF IC Card Sensor Module + S50 Blank Card | Safety | B07VLDSYRW | B07VLDSYRW | 1 | $9.99 | $9.99|
|ELEGOO MEGA R3 Board|ATmega+2560 micro-controller board| Safety|B01H4ZLZLQ|ELEGOO| 1 |Provided by student | N/A|
| **Total** |  |  |  | **Total Components** | 1 | **Total Cost** | $9.99 |
