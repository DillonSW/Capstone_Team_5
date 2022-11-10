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
![Schematic]("C:\Users\dillo\Downloads\GetImage.jpeg")  

