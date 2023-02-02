## Function

This subsystem's function in our design is to tie all of the subsystems together, providing appropriate power to each system. The power coming from the wall outlet will be sent through terminal blocks in our din rail. This 120VAC power will be sent to the PC, and will be converted to 24VDC and sent to the PLC and sensor subsystem.

## Constraints

**The 120VAC wall power:**
* **Will be protected by a GFCI cable**

* **Will go through a circuit breaker as extra protection for our power system**
^ The 120VAC will feed through a circuit breaker on the din rail, then be sent to the PC and the 120VAC to 24VDC power supply.

* **Will power the PC**
^ A mini PC or "trashcan PC" may have needed a stepped-down voltage. But because we needed more RAM to run our database and communication servers, a regular PC must be used. These PCs can handle 120VAC input power.

* **Will be stepped down from 120VAC to 24VDC through the use of a power supply block**
^ This 24VDC will be used to power the PLC and Sensor systems. From there, the PLC will also output 24VDC to control all hardware.

**The 120VAC electrical components:**
* **Will be secured and protected within an enclosure**
^ This closure will be grounded and the components will be secured in this panel enclosure to ensure the safety of personnel and the machine.

## Schematic

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Power-Subsystem/images/PowerSchemOne.jpg)

Din rail connections, circuit breaker, 120VAC to 24VDC power supply for PLC. Three 24VDC hots are jumped and three 24VDC neutrals are jumped and going to the sensor system.

## Analysis

The din rail and the mounted components must fit within a certain space. We were told by the mechanical team that we will have roughly 35 inches of width to work with. Each component's width will be measured and a subpanel and enclosure will be chosen accordingly.

**Note**
The Hot/Neutral Terminals were rounded up from 0.244 to 0.25.

The Ground Terminals were rounded up from 0.24 to 0.25.

The End Covers were rounded up from 0.0866 inches to 0.1 inch, which is a roughly 15% increase. This gives the end covers a 15% pre-calculation tolerance.

The PLC dimensions claim to be 3.937 inches wide. Hand-measured dimensions were 5.125 inches wide. These calculations are using 5.125 inches.

^ Source: https://www.automation24.com/siemens-cpu-1215c-6es72151ag400xb0?gclid=CjwKCAiAuOieBhAIEiwAgjCvcgl-DwwSXIfjnvM5ExyufzDYwyMGhMjmCjiGZCoLiI1Ku4H43bPSvRoC6qcQAvD_BwE


| Component | Width (inches) | Quantity | Total Width |
|-----------|-------|----------|------------|
| Hot/Neutral Terminal Blocks | 0.25 | 11 | 2.75 |
| Ground Terminal Blocks | 0.25 | 2 | 0.5 |
| End Covers | 0.1 | 5 | 0.5 |
| Stop Blocks (End Anchors) | 0.31 | 10 | 3.1 |
| Circuit Breaker | 0.69 | 1 | 0.69 |
| PLC | 5.125 | 1 | 5.125 |
|**Total** |  | **Total Width (inches):** | 12.665 |

Without rounding, the actual measurements came out to be 12.512in.

We are choosing a subpanel with a width of 15in. This gives us 2.325 to 2.488in of clearance. Given how small the terminals are, there is enough room to place 7 to 8 additional terminals if needed.

## BOM

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| Terminal Blocks | 32A, 1000V, Feed Through, Screw, 26-10 AWG | Power | 3044102 | Phoenix Contact | 11 | $1.18 | $12.98 |
| Ground Terminals | 800V, Feed Through, Screw, 26-10 AWG | Power | 1010100000 | Weidmuller | 2 | $7.43 | $14.86 |
| Terminal Covers | End Cover Brackets | Power | 3047028 | Phoenix Contact | 5 | $0.82 | $4.10 |
| 2-Block Jumpers | Flat Pin Cross Connection, 2 Positions | Power | 3030161 | Phoenix Contact | 2 | $0.88 | $1.76 |
| 3-Block Jumpers | Flat Pin Cross Connection, 3 Positions | Power | 3030174 | Phoenix Contact | 3 | $1.80 | $5.40 |
| End Anchors | Snap-On, Din Rail End Anchors | Power | 1492-EAJ35 | Allen Bradley | 10 | $2.42 | $24.20 |
| Circuit Breaker | 1-Pole, C Curve, 240VAC/60VDC, 32A, 18-2 AWG Circuit Breaker | Power | 1492-SPM1C320 | ASI | 1 | $8.48 | $8.48 |
| 24VDC Power supply | 120VAC to 120W, 24V, Din Rail Power Supply | Power | SVL524100 | Sola-HD | 1 | $74.59 | $74.59 |
| Wire Duct | 1.26in Wide, 1in Depth, Slotted, Lead-Free PVC, Screw Mount Wire Duct | Power | F1X1LG6-A | Panduit | 1 | $29.02 | $29.02 |
| Wire Duct Cover | 1.26in Wide, 1in Depth, PVC, Flush Wire Duct Cover | Power | C1LG6-F | Panduit | 1 | $7.05 | $7.05 |
| Enclosure | 14H x 16W x 6D (in), Wall-Mount, Single Door, Stainless Steel Clamp Enclosure | Power | SCE-1614CHSNF | Saginaw | 1 | $186.00 | $186.00 |
| Subpanel | 13H x 15W (in), 14 Gauge, Carbon Steel Subpanel | Power | SCE-16P14 | Saginaw | 1 | $29.50 | $29.50 |
| **Total** |  |  |  | **Total Components** | 39 | **Total Cost** | $397.94 |
