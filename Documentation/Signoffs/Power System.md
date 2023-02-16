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

This means that we will be able to use our enclosure as an effective ground-fault to protect users, administrators, and maintenance personnel that may be working near the electrical components.

**These constraints will be labeled C1-C6 in the Analysis section**

## Schematic

**Note: The wires are labeled as the terminal block or component that they are feeding TO, not FROM. Ex. TB02-1 or PLC24L-1.**

Also, the **Motor Driver**, **Sensors**, and **Safety Sensors** have been heavily simplified for convenience of the power system wiring. To see the schematics of the simplified components, please refer to the **Motor System**, **Sensor System**, and **Safety System**.

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Power-Subsystem/images/PowerSchemTwo.jpg)

The schematic above shows how the power system will tie every subsystem together. The terminal blocks that are larger than 1x1 indicate that they have been jumped together. The wires feeding into and out of the terminal blocks are also labeled based on what component they are connected to. For consistency, the top wire will be labeled [Name]-1 and the bottom wire will be labeled [Name]-2.

The larger terminal blocks, as stated before, are connected through jumpers. We are buying these jumpers as 10-position connectors. The framework for these jumpers are made of metal. We will cut down the 10-position ones into smaller positions as needed (ex: 2 or 3) with the help of the tools in our machine shops.

## Analysis

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

## BOM

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| Terminal Blocks | 20A, 600V, Feed Through, Screw, 26-10 AWG | Power | KN-T12GRY-25 | Konnect-It | 1 (Pack of 25) | $8.50 | $8.50 |
| Ground Terminals | 800V, Feed Through, Screw, 26-10 AWG | Power | 1010100000 | Weidmuller | 3 | $4.27 | $12.81 |
| Terminal Covers | End Cover Brackets | Power | KN-ST1GRY | Konnect-It | 1 (Pack of 25) | $11.00 | $11.00 |
| 10-Block Jumpers | Screw-Down, 10 Positions | Power | KN-10J12 | Konnect-It | 1 (Pack of 5) | $10.50A | $10.50 |
| End Anchors | Snap-On, Din Rail End Anchors | Power | 1492-EAJ35 | Allen Bradley | 10 | $2.42 | $24.20 |
| Circuit Breaker | 1-Pole, C Curve, 240VAC/60VDC, 32A, 18-2 AWG Circuit Breaker | Power | 1492-SPM1C320 | ASI | 1 | $8.48 | $8.48 |
| 24VDC Power supply | 120VAC to 120W, 24V, Din Rail Power Supply | Power | SVL524100 | Sola-HD | 1 | $70.88 | $70.88 |
| Wire Duct | 1.26in Wide, 1in Depth, Slotted, Lead-Free PVC, Screw Mount Wire Duct | Power | F1X1LG6-A | Panduit | 1 | $29.02 | $29.02 |
| Wire Duct Cover | 1.26in Wide, 1in Depth, PVC, Flush Wire Duct Cover | Power | C1LG6-F | Panduit | 1 | $7.05 | $7.05 |
| Enclosure | 14H x 16W x 6D (in), Wall-Mount, Single Door, Stainless Steel Clamp Enclosure | Power | SCE-1614CHSNF | Saginaw | 1 | $186.00 | $186.00 |
| Subpanel | 13H x 15W (in), 14 Gauge, Carbon Steel Subpanel | Power | SCE-16P14 | Saginaw | 1 | $29.50 | $29.50 |
| Din Rail | 19.7-inch, Slotted, Steel Din Rail | Power | 467406 | RS PRO | 1 | $4.99 | $4.99 |
| Power Cord | GFCI, 9-ft Length, 16 AWG, 15A, 120VAC, IEC320 Power Cable | Power | 2XYT2 | NEMA | 1 | $47.84 | $47.84 |
| Cable Entry Plate | 35 Entry, Screw Mounting Cable Entry | Power | KEL-DPZ 63/35 | Icotek | 2 | $26.11 | $52.22 |
| M12 Cable Gland | M12, Waterproof, Adjustable, Locknut, 3-6mm, Nylon Cable Gland | Power | A16101800ux0286 | uxcell | 1 | $6.49 | $6.49 |
| Fuse Terminal | W-Series Fuse Block | Power | 402363 | Weidmüller | 1 | $6.61 | $6.61 |
| Danger Sign | 120V OSHA Danger Sign, 3.5" x 5" | Power | S-2260 | MySafetySign | 1 | $5.20 | $5.20 |
| **Total** |  |  |  | **Total Components** | **REDO** | **Total Cost** | **REDO** |
