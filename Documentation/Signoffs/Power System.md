## Function

This subsystem's function in our design is to tie all of the subsystems together, providing appropriate power to each system. The power coming from the wall outlet will be sent through terminal blocks in our din rail. This 120VAC power will be sent to the PC, and will be converted to 24VDC and sent to the PLC and sensor subsystem.

## Constraints

**The 120VAC wall power:**
* **Will go through a circuit breaker as extra protection for our power system**

^ The 120VAC will feed through a circuit breaker on the din rail, then be sent to the PC, motor driver, and the 120VAC to 24VDC power supply.

* **Will power the PC**

^ A mini PC or "trashcan PC" may have needed a stepped-down voltage. **But because we needed more RAM to run our database and communication servers, a regular PC must be used. These PCs can handle 120VAC input power.**

* **Will be stepped down from 120VAC to 24VDC through the use of a power supply block**

^ This 24VDC will be used to power the PLC and Sensor systems. From there, the PLC will also output 24VDC to control all hardware.

**The 120VAC electrical components:**
* **Will be secured and protected within an enclosure**

^ This closure will be grounded and the components will be secured on a din rail, attached to the subpanel, in the enclosure to ensure the safety of personnel and the machine.

**All of the components**
* **Must be able to fit within an enclosure that can fit within a 35-inch wide space.**

This is the width that we were given by the mechanical team for housing our electrical components.

**The enclosure**
* **Will be grounded and serve in accordance with NEC 250.109**

^ This NEC standard states that "Metal enclosures shall be permitted to be used to connect bonding jumpers or equipment grounding conductors, or both, together to become a part of an effective ground-fault current path. Metal covers and metal fittings attached to these metal enclosures shall be considered as being connected to bonding jumpers or equipment grounding conductors, or both."

^ Source: https://www.electricallicenserenewal.com/Electrical-Continuing-Education-Courses/NEC-Content.php?sectionID=870.0

This means that we will be able to use our enclosure as an effective ground-fault to protect users, administrators, and maintenance personnel that may be working near the electrical components. We will also have a GFCI power cord for additional safety.

**These constraints will be labeled C1-C6 in the Analysis section**

## Schematic

![EnclosurePosition1](https://user-images.githubusercontent.com/113734069/219280985-e76c1219-3334-4040-b722-47e2a1459e6f.jpg)
![EnclosurePosition2](https://user-images.githubusercontent.com/113734069/219280999-b0b13ac5-40e4-4450-a575-0c6b3cf87040.jpg)
![EnclosurePosition3](https://user-images.githubusercontent.com/113734069/219281010-9f2259ca-2599-4fce-b3e5-4c555603b9e6.jpg)
![EnclosurePosition4](https://user-images.githubusercontent.com/113734069/219281020-d15d8dc8-8d0c-407b-9819-c46f2a80dfa4.jpg)

![Dinrail_Layout](https://user-images.githubusercontent.com/113734069/219281039-ca8d7a82-879d-47a6-bf2b-7a8fdc0cf0a2.jpg)
![RailLayout_Left](https://user-images.githubusercontent.com/113734069/219281047-c0387b83-931b-4a76-b368-753b8338ceca.jpg)
![RailLayout_Mid](https://user-images.githubusercontent.com/113734069/219281056-31ba6f4f-c1c3-4ce2-8006-d8e13b2c9872.jpg)
![RailLayout_Right](https://user-images.githubusercontent.com/113734069/219281063-6418875c-b393-4724-9358-cc104df3ed8c.jpg)


**Note: The wires are labeled as the terminal block or component that they are feeding TO, not FROM. Ex. TB02-1 or PLC24L-1.**

Also, the **Motor Driver**, **Sensors**, and **Safety Sensors** have been heavily simplified for convenience of the power system wiring. To see the schematics of the simplified components, please refer to the **Motor System**, **Sensor System**, and **Safety System**.

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Power-Subsystem/images/PowerSchemTwo.jpg)

The schematic above shows how the power system will tie every subsystem together. The terminal blocks that are larger than 1x1 indicate that they have been jumped together. The wires feeding into and out of the terminal blocks are also labeled based on what component they are connected to. For consistency, the top wire will be labeled [Name]-1 and the bottom wire will be labeled [Name]-2.

The larger terminal blocks, as stated before, are connected through jumpers. We are buying these jumpers as 10-position connectors. The framework for these jumpers are made of metal. We will cut down the 10-position ones into smaller positions as needed (ex: 2 or 3) with the help of the tools in our machine shops.

## Analysis

## Constraints C3, C4, C6

These constraints are fulfilled through our enclosure and subpanel design. The KiCAD schematics above confirm that we will be using stepping down our 120VAC voltage (**C6**) and that the enclosure will be grounded (**C3**). The AutoCAD and SolidWorks schematics confirm that we will be using an enclosure (**C4**).

## Constraint C5

The din rail and the mounted components must fit within a certain space. We were told by the mechanical team that we will have roughly 35 inches of width to work with. Each component's width will be measured and a subpanel and enclosure will be chosen accordingly.

**Note**
The Hot/Neutral Terminals were rounded up from 0.20 inches to 0.25 inches, a 25% increase for tolerance.

The Ground Terminals were rounded up from 0.24 inches to 0.25 inches.

The End Covers were rounded up from 0.0866 inches to 0.1 inch, which is a roughly 15% increase. This gives the end covers a 15% pre-calculation tolerance.

The fuse terminal is 8mm (or 0.315 inches), which will be rounded up to .320 inches.

The PLC dimensions claim to be 3.937 inches wide. Hand-measured dimensions were 5.125 inches wide. These calculations are using 5.125 inches.

^ Source: https://www.automation24.com/siemens-cpu-1215c-6es72151ag400xb0?gclid=CjwKCAiAuOieBhAIEiwAgjCvcgl-DwwSXIfjnvM5ExyufzDYwyMGhMjmCjiGZCoLiI1Ku4H43bPSvRoC6qcQAvD_BwE


| Component | Width (inches) | Quantity | Total Width |
|-----------|-------|----------|------------|
| Hot/Neutral Terminal Blocks | 0.25 | 14 | 3.5 |
| Ground Terminal Blocks | 0.25 | 3 | 0.75 |
| End Covers | 0.1 | 5 | 0.5 |
| Stop Blocks (End Anchors) | 0.31 | 10 | 3.1 |
| Circuit Breaker | 0.69 | 1 | 0.69 |
| PLC | 5.125 | 1 | 5.125 |
| Fuse Block | .320 | 1 | .320 |
|**Total** |  | **Total Width (inches):** | 13.985 |

Without rounding, the actual measurements came out to be 13.183 inches.

We are choosing a subpanel with a width of 15in. This gives us 1.015 inches of clearance. With rounding, we have 1.817 inches. Given how small the terminals are, there is enough room to place 5 or 9 additional terminal blocks respectively.

## Constraints C1 and C2

**Analysis for 120V-side current draw**

To determine the power cord and circuit breaker, we must analyze how much current each 120VAC component will draw. The following is a list of the components and their draws.

* 120VAC to 24VDC Power Supply (120 Side): **1A**
$V1 * I1 = V2 * I2$

$V1 = 120$, $I2(Max) = 5A$, $V * I = 120W$

$120 * I1 = 120$

These equations give that the 120V side will draw, at max, 1A. The 24V side will draw, at max, 5A. **The 24V side will be further analyzed to see how much current it will actually draw**

* PC: **700mA**

The ThinkCentre PC stickers show that the PC-side of the power block draws 20V, 3.5A.

$120V * I1 = 20V * 3.5A$

$I1 = .7A$

* Motor Driver: **2.5A**

The motor driver datasheet states that it will draw 2.5A. Please refer to the Motor System branch to find the datasheet.

**Total 120V-side current draw**

$1 + .7 + 2.5 = 4.2A$

Assuming that 4.2A is 80% of max capacity, we must have a circuit breaker that is at least 5.25A. We will use a 6A circuit breaker.

We also want the circuit breaker to be higher rated than the power cord. We will use a 5A GFCI power cord.

**Analysis for 24-side current draw**

To determine the fuse breaker protecting the 24VDC components, we must analyze their current draw of all of the components.

* PLC: **1.5A**

The side of the PLC states that it will draw 1.5A.

* Box Sensors: **.025A each**

There are 3 box sensors (top, middle, bottom). Therefore the total current draw will be **.075A**.

* Safety Sensors: **.2A each**

There are also 3 safety sensors (top, middle, bottom). Therefore the total current draw will be **.6A**.

**Total 24V-side current draw**

$1.5 + .075 + .6 = 2.175$

Assuming that 2.175A is 80% of max capacity, we must have a fuse breaker that is at least 2.72A. We will use a 3A fuse breaker.

## BOM

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| Terminal Blocks | 20A, 600V, Feed Through, Screw, 26-12 AWG | Power | KN-T12GRY-25 | Konnect-It | 1 (Pack of 25) | $8.50 | $8.50 |
| Ground Terminals | 800V, Feed Through, Screw, 26-12 AWG | Power | 1010100000 | Weidmuller | 3 | $4.27 | $12.81 |
| Terminal Covers | End Cover Brackets | Power | KN-ST1GRY | Konnect-It | 1 (Pack of 25) | $11.00 | $11.00 |
| 10-Block Jumpers | Screw-Down, 10 Positions | Power | KN-10J12 | Konnect-It | 1 (Pack of 5) | $10.50A | $10.50 |
| End Anchors | Snap-On, Din Rail End Anchors | Power | 1492-EAJ35 | Allen Bradley | 10 | $2.42 | $24.20 |
| Circuit Breaker | 1-Pole, C Curve, 277VAC/48VDC, 4Amp Circuit Breaker | Power | FAZ-D4-1-SP | Eaton | 1 | $15.00 | $15.00 |
| Circuit Breaker | 1-Pole, D Curve, 277VAC/48VDC, 2Amp Circuit Breaker | Power | FAZ-D2-1-SP | Eaton | 1 | $15.00 | $15.00 |
| 24VDC Power supply | 120VAC to 120W, 24V, Din Rail Power Supply | Power | SVL524100 | Sola-HD | 1 | $70.88 | $70.88 |
| Wire Duct | 1.26in Wide, 1in Depth, Slotted, Lead-Free PVC, Screw Mount Wire Duct | Power | F1X1LG6-A | Panduit | 1 | $29.02 | $29.02 |
| Wire Duct Cover | 1.26in Wide, 1in Depth, PVC, Flush Wire Duct Cover | Power | C1LG6-F | Panduit | 1 | $7.05 | $7.05 |
| Enclosure | 12H x 10W x 6D (in), Wall-Mount, Single Door, Carbon Steel Enclosure | Power | SCE-1210ELJ | Saginaw | 1 | $107.00 | $107.00 |
| Subpanel | 12H x 9W (in), 14 Gauge, Carbon Steel Subpanel | Power | SCE-12P10 | Saginaw | 1 | $11.50 | $11.50 |
| Din Rail | 19.7-inch, Slotted, Steel Din Rail | Power | 467406 | RS PRO | 1 | $4.99 | $4.99 |
| Power Cord | GFCI, 10-ft, In-Line, Vending Machine Cord | Power | 30376018-01 | Tower Manufacturing Corporation | 1 | $77.76 | $77.76 |
| Power Splitter | 2-ft, 14 AWG, 3-Splitter Power Extension | Power | PW163-1324 | Nema | 1 | $6.80 | $6.80 |
| Splitter Cords | 6-ft, 14 AWG Power Cord | Power | PW116-1206 | Nema | 3 | $4.74 | $14.22 |
| Cable Entry Plate | 14 Entry, Screw Mounting Cable Entry | Power | KEL-DPZ 63/14 | Icotek | 1 | $26.11 | $26.11 |
| M12 Cable Gland | M12, Waterproof, Adjustable, Locknut, 3-6mm, Nylon Cable Gland | Power | A16101800ux0286 | uxcell | 2 | $6.49 | $12.98 |
| Fuse Terminal | W-Series Fuse Block | Power | 402363 | Weidmüller | 1 | $6.61 | $6.61 |
| Fuse | Fast-Acting 3A Fuse Breaker | Power | A-02-GSZ-7-DB | Eaton Bussman | 1 (Pack of 4) | $9.99 | $9.99 |
| Danger Sign | 120V OSHA Danger Sign, 3.5" x 5" | Power | S-2260 | MySafetySign | 1 | $5.20 | $5.20 |
| **Total** |  |  |  | **Total Components** | 31 | **Total Cost** | $588.19 |
