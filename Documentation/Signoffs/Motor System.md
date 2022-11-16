# Motor System

## Subsystem Function

This subsystem's role in our design is to move new devices to the checkout door by receiving power from our power subsystem and rotating the platforms holding the devices. This will only be done when the machine senses that there is a device missing from the checkout drawer. After discussing with the mechanical engineering team, we have decided to make the platforms out of acrylic and the hollow tube inside our machine to be either **aluminum** or **pvc**.  
 
## Constraints

* **The boards being rotated on the platforms (box and all) will weigh 0.5lbs**  
**The platforms being rotated by the motor:**  
* **Will hold 20 boards (10 lbs)**

* **Will be made out of acrylic **  

* **Will be 3.175 mm (1/8 inch) thick, 3 feet in diameter, and have a 16" hollowed diameter in the center.**  
^ This will make the platforms like hollow rings. 

* **Will weigh 3.937 lbs each**  
^ 1/8" acrylic weighs 0.694 lbs/sq. ft. https://www.usplastic.com/knowledgebase/article.aspx?contentkey=884 
Area of circle = 78.540% area of square with same diameter: (pi*0.5^2)/1 = 0.78540  
(Weight of whole, 3' diameter, 1/8" thick circle) - (Weight of missing, 16" diameter, hollow center) = 4.906 - 0.969 = **3.937**.  
Material of platform: Acrylic  

* **The platforms will have a flexural strength of at least 4351.13 PSI** 
^ The lowest flexural strength of 64 cast glass specimens was 30 MPA, which equates to 4351.13 PSI. Even though the flexural strength of acrylic is x3 or more that of glass, assuming acrylic's flexural strength is equal to glass can be our worst-case scenario.  
^ Source: https://link.springer.com/article/10.1007/s40940-021-00151-z  
Flexural Strength: 16,500 PSI (6mm thickness)  
^ Source: https://www.builditsolar.com/References/Glazing/physicalpropertiesAcrylic.pdf  

* **Given these calculations, the total weight of the platforms and boards will be 44.811 lbs.**

**The dividers on each platform:**
* **Will also be made of acrylic**  

* **Will be 1/16th inch thick (giving a density of 0.365 lbs/ sq. ft.)**  

* **Will be large enough to encompass the whole board (8.5 x 8 inches, will assume 9 x 9 inches).**  
^ There will be 20 dividers per platform, equating to 60 total platforms.  

* **Given these values, each divider will weigh 0.27375 lbs (0.365 * 0.75). The total weight of the dividers will be 16.425 lbs.**  

**The hollow cylinder supporting the platforms:**  
* **Will be made of aluminum or pvc (assuming aluminum for worst-case)**  

* **Will be 36- to 40-inches tall (assuming 40 inch for worst-case).**  

* **Will be 1/16th or 1/8th thick (assuming 1/8th inch for worst-case).**  
^ Given the density of aluminum (2.7 g/cm^3) and given the area equation for a hollow cylinder  

M = πhmD(r^2 - (r - t)^2)  
where:  
  M = mass of the hollow cylinder
  h = height  
  r = outer radius  
  t = thickness  
  mD = Mean Density of cylinder material  
The hollow aluminum cylinder will weigh **9.622 lbs**  

**The Motor:  **
* **Given the calculations above, must rotate a total weight of 70.858 lbs. (We will assume roughly 5% tolerance for error, so for calculations we will use 75 lbs)**  
 
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
![Motor](https://github.com/DillonSW/Capstone_Team_5/blob/main/images/MotorSchematic.jpg)

This is the schematic for the stepper motor our team is looking to use, the E Series Nema 34 Stepper Motor. This motor has a holding torque of 12 Nm (or 106.29 lb-in). The calculations that led us to this decision is in Analysis. If we are able to go with this motor, we will need a driver. There is a driver built specifically for the Nema 34: The HSS86 Hybrid Step Servo.  
^ Source: https://www.omc-stepperonline.com/download/34HE59-6004S.pdf  

**Driver**  
<img src="https://github.com/DillonSW/Capstone_Team_5/blob/main/images/DriverSchematic.jpg" width=50% height=50%>  

This is the schematic for the frame of the servo, mainly used for implementation into a machine. All measurements are in mm.  
^ Source: https://www.jbcnc.se/images/datasheets/HSS86.pdf  

<img src="https://github.com/DillonSW/Capstone_Team_5/blob/main/images/DriverWiring.jpg" width=50% height=50%>  
This is the wiring diagram for the driver and how it connects to the motor and step encoding. The resistors shown can vary, but because the signal control voltage will be +12V, the input port will need to be connected to a 1KΩ-2KΩ resistor.  

## Analysis

As stated previously, the motor must be able to output enough torque to rotate roughly 75 lbs. Our current machine design is a hollow cylinder, with the outer diameter being 3' and the inner, hollow diameter being roughly 1'4"  

T=W(R1^2+R2^2)/2∗∆N/308t

The equation above is for calculating the torque required to move a certain weight in a hollow cylinder.  

The variables above are defined as:  
T = Required Torque, lb-ft  
WK^2 = Mass Moment of Inertia of load to be accelerated lb-ft^2  
∆N = Change of Speed, rpm  
t = time to accelerate the load, seconds  
W = weight of object, lb  
R1 = outside radius of cylinder, ft  
R2 = inside radius of cylinder, ft  

^ Source: https://www.engineersedge.com/motors/hollow_cylinder_axis_torque_force_equation.htm  

The values of W, R1, & R2 Are consistence since they are the current constraints of our design:  
W = 75 lb 

R1 = 1.5 ft 

R2 = 0.666 ft 

While the values of ∆N & t will vary for testing purposes: 

∆N1 = 5 rpm 

∆N2 = 3 rpm 

∆N2 = 1 rpm 

t1 = 0.25 sec 

t2 = 0.5 sec 

t2 = 1 sec  

Our current goal is for the rotary device to take roughly 3 seconds to transition from 1 compartment to another. The device would need to rotate 18° to have a complete transition. Luckily for us our choice of stepper motor makes it so each step is 1.8°, which makes it so we have to take exactly 10 steps to reach the next compartment. Using this information, we can determine that are desired rpm will be roughly 1 rpm since 18°/3 sec =6° per second.  

To find the motor that would work best for our project  

Stepper Motors are DC motors that divided a full rotation into a set of equal steps. This will give us greater control on speed and movement of our motor, and the math happens to work in our favor.  

To know what type of stepper motor we need, we have to calculate the torque it will need to properly rotate our device.  

With the known values above, and the values that can be varied, a torque calculation table can be created for each case:  

**Givens:**  
W = 75 lbs  
R1 = 1.5 ft  
R2 = 0.67 ft  

**Required Torque Calculations (lb-ft) **
|  t(s)  |         ∆N (rpm)         |  
|--------|--------------------------|
|        |    1   |    2   |    3   |
|  0.25  | 1.3122 | 3.9367 | 6.5611 |
|  0.5   | 0.6561 | 1.9683 | 3.2806 |
|    1   | 0.3281 | 0.9842 | 1.6403 |  

As shown above, the highest amount of torque required would be at 5 rpm, accelerating in 0.25 seconds. This torque would be 8.8957 Nm.  
However, these results are assuming that a DC motor will be 100% efficient when operating at a lower rated load. This is an unreasonable expectation. Most DC motors are designed to be anywhere from 50-100% efficient with peak efficiency being at around 75% of the rated load. So for a 12 Nm motor, the optimal load range is from 6 to 12 Nm, with peak being at 9 Nm. Because we would have at most 8.8957 Nm of required torque, and an assumed efficiency of 50% the most torque requited would be 17.7914 Nm. However we are deciding to run the motor assuming a lower acceleration time and rpm. At the values we are expecting to run (0.5s acceleration and 3 rpm), also assuming 50% efficiency, the required torque would be 5.3374 Nm, which is an acceptable level for our desired motor. 

^ Source: https://www.energy.gov/sites/prod/files/2014/04/f15/10097517.pdf 

Since the motor we are looking at can have a holding torque of 12 Nm, it will meet the constraints of outputting enough torque and securing the devices. We would be able to operate the motor at a lower demand than its maximum, putting less strain on the motor over time.  

## BOM

<img src="https://github.com/DillonSW/Capstone_Team_5/blob/main/images/MotorBOM.jpg" width=100% height=100%>

