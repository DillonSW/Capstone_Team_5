## Function

This subsystem's function in our design is to tie all of the subsystems together, providing appropriate power to each system. The power coming from the wall outlet will be sent through terminal blocks in our din rail. This 120VAC power will be sent to the PC, and will be converted to 24VDC and sent to the PLC and sensor subsystem.

## Constraints

.

## Schematic

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Power-Subsystem/images/PowerSchemOne.jpg)

Din rail connections, circuit breaker, 120VAC to 24VDC power supply for PLC. Three 24VDC hots are jumped and three 24VDC neutrals are jumped and going to the sensor system.

## Analysis

.

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
