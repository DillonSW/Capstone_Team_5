# Motor System

## Subsystem Function

This subsystem's role in our design is to move new devices to the checkout door by receiving power from our power subsystem and rotating the platforms holding the devices. This will only be done when the machine senses that there is a device missing from the checkout drawer. 

## Constraints

**Background for Constraints**
Total weight of boards rotated per platform: 10 lbs  

Material of platform: Acrylic  

Flexural Strength: 16,500 PSI (6mm thickness)  

^ Source: https://www.builditsolar.com/References/Glazing/physicalpropertiesAcrylic.pdf    Tested by ASTM D790  

We are going to try to use 3.175mm (1/8") thick acrylic in order to reduce the total weight. Given a flexural strength of 16,500 PSI for 6mm thickness, going to 3.175 should not make the platform flex under 10 lbs.  

Weight of 3-ft diameter acrylic: Assuming 1/8'" thickness, a 3 sq. ft. square acrylic sheet weighs 6.246 lbs (0.694 lbs/sq. ft.) Given that a circle with a diameter equal to the side length of a square has 78.540% of the area, a 3-ft diameter, 3.175mm thick, acrylic circle weighs 4.906 lbs.   

* **Given these estimated values, and that there will be 3 platforms in the machine, the motor must output enough torque to rotate roughly 44.717 lbs. (For calculations, we will round to 45 lbs.)**
  * This is also assuming that the acrylic circle will be solid throughout, which will not be the case for the vending machine. The inner 1'4" diameter will be hollowed out for components and sensors. Assuming that the acrylic will be solid throughout gives us torque calculations higher than what will be reality. This makes sure that if the constraints are met, they will definitely be met during the testing. 

* **The motor will receive 24VDC from the power system.**
* **The motor will be a stepper motor.**  
This is because a stepper motor divides a full rotation into a certain amount of equal steps. A stepper motor can do this by having groups of coils called "phases."  
When a "phase" is energized, the stepper motor will rotate by one step. The motor will only move on to the next step if the next "phase" group is energized.  

^ Source: https://learn.adafruit.com/all-about-stepper-motors  
* **The motor will be protected at the nameplate current rating (6A).**  
This is because a stepper motor divides a full rotation into a certain amount of equal steps. A stepper motor can do this by having groups of coils called "phases." When a "phase" is energized, the stepper motor will rotate by one step. The motor will only move on to the next step if the next "phase" group is energized. 

^ Source: https://learn.adafruit.com/all-about-stepper-motors  
240.4(B) is the standard for overcurrent devices rated 800 amperes or less, which allows the use of a higher rated overcurrent device as long as the conditions are met. All of these conditions have been cleared.  
 * The conductors being protected are not part of a branch circuit supplying more than one receptacle for cord-and-plug-connected portable loads.  
 * The ampacity of the conductors does not correspond with the standard ampere rating of a fuse or a circuit breaker without overload trip adjustments above its rating (but that shall be permitted to have other trip or rating adjustments).  
 * The next higher standard rating selected does not exceed 800 amperes.  
  
^ Source: https://up.codes/viewer/illinois/nfpa-70-2020/chapter/2/wiring-and-protection#240.4_(B)  

## Schematic

**Motor**  
![Motor](https://github.com/DillonSW/Capstone_Team_5/blob/main/images/DriverSchematic.jpg)

This is the schematic for the stepper motor our team is looking to use, the E Series Nema 34 Stepper Motor. This motor has a holding torque of 12 Nm (or 106.29 lb-in). The calculations that led us to this decision is in Analysis. If we are able to go with this motor, we will need a driver. There is a driver built specifically for the Nema 34: The HSS86 Hybrid Step Servo.  
^ Source: https://www.omc-stepperonline.com/download/34HE59-6004S.pdf  

**Driver**  
<img src="https://github.com/DillonSW/Capstone_Team_5/blob/main/images/DriverSchematic.jpg" width=50% height=50%>  

This is the schematic for the frame of the servo, mainly used for implementation into a machine. All measurements are in mm.  
^ Source: https://www.jbcnc.se/images/datasheets/HSS86.pdf  

<img src="https://github.com/DillonSW/Capstone_Team_5/blob/main/images/DriverWiring.jpg" width=50% height=50%>  
This is the wiring diagram for the driver and how it connects to the motor and step encoding. The resistors shown can vary, but because the signal control voltage will be +12V, the input port will need to be connected to a 1KΩ-2KΩ resistor.  

## Analysis

As stated previously, the motor must be able to output enough torque to rotate roughly 45 lbs. Our current machine design is a hollow cylinder, with the outer diameter being 3' and the inner, hollow diameter being roughly 1'4"  

T=W(R21+R22)2∗∆N308t

The equation above is for calculating the torque required to move a certain weight in a hollow cylinder.  

The variables above are defined as:  
