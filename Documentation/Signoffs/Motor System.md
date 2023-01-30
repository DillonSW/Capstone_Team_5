# Motor System

## Subsystem Function

This subsystem's role in our design is to move new devices to the checkout door by receiving power from our power subsystem and rotating the platforms holding the devices. This will only be done when the machine senses that there is a device missing from the checkout drawer. After discussing with the mechanical engineering team, we have decided to make the platforms out of acrylic and the hollow tube inside our machine to be either **aluminum** or **pvc**.  
 
## Constraints

* **The boards being rotated on the platforms (box and all) weigh 0.5lbs**  
^ Each platform will be able to hold 20 boards

**The platforms being rotated by the motor:**  
* **Will be made out of acrylic**  

* **Will be 3.175 mm (1/8 inch) thick, 3 feet in diameter, and have a 16" hollowed diameter in the center.**  
^ This will make the platforms like hollow rings. 

* **Will weigh 3.937 lbs each**  
^ 1/8" acrylic weighs 0.694 lbs/sq. ft. https://www.usplastic.com/knowledgebase/article.aspx?contentkey=884 
Area of circle = 78.540% area of square with same diameter: $(pi*0.5^2)/1 = 0.78540$  
(Weight of whole, 3' diameter, 1/8" thick circle) - (Weight of missing, 16" diameter, hollow center) = 4.906 - 0.969 = **3.937**.  
Material of platform: Acrylic  

* **The platforms will have a flexural strength of at least 4351.13 PSI** 
^ The lowest flexural strength of 64 cast glass specimens was 30 MPA, which equates to 4351.13 PSI. Even though the flexural strength of acrylic is x3 or more that of glass, assuming acrylic's flexural strength is equal to glass can be our worst-case scenario.  
^ Source: https://link.springer.com/article/10.1007/s40940-021-00151-z  
Flexural Strength: 16,500 PSI (6mm thickness)  
^ Source: https://www.builditsolar.com/References/Glazing/physicalpropertiesAcrylic.pdf  

* **Given these calculations, the total weight of the platforms and boards will be 44.811 lbs.**

* **The platforms will also have a 1 in. gap between them and the frame of the machine.**

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

$M = (π)(h)(mD)(r^2 - (r - t)^2)$  
where:  
  M = mass of the hollow cylinder
  h = height  
  r = outer radius  
  t = thickness  
  mD = Mean Density of cylinder material  
The hollow aluminum cylinder will weigh **9.622 lbs**  

**The Motor:**
* **Given the calculations above, must rotate a total weight of 70.858 lbs. (We will assume roughly 20% tolerance for error, so for calculations we will use 85 lbs)**

**Circuity:** 
* **Will be protected at 125% the nameplate current rating (3.19A).** This comes from the following codes.

The standard NEC 430.52(D) states "Torque motor branch circuits shall be protected at the motor nameplace current rating in accordance with 240.4(B)

^ Source: https://up.codes/s/rating-or-setting-for-individual-motor-circuit

NEC 240.4(B) is the standard for overcurrent devices rated 800 amperes or less, which allows the use of a higher rated overcurrent device as long as the conditions are met. All of these conditions have been cleared.  
 * The conductors being protected are not part of a branch circuit supplying more than one receptacle for cord-and-plug-connected portable loads.  
 * The ampacity of the conductors does not correspond with the standard ampere rating of a fuse or a circuit breaker without overload trip adjustments above its rating (but that shall be permitted to have other trip or rating adjustments).  
 * The next higher standard rating selected does not exceed 800 amperes.  
^ Source: https://up.codes/viewer/illinois/nfpa-70-2020/chapter/2/wiring-and-protection#240.4_(B)  

The standard NEC 705.12(D)(2) Bus or Conductor Ampere Rating states "One hundred twenty-five percent [125%] of the inverter output circuit current shall be used in ampacity calculations for the following: Feeders, Taps, and Busbars."

^ Source: https://up.codes/viewer/delaware/nfpa-70-2014/chapter/7/special-conditions#705.12_(D)_(2)

* **Will follow the NEC 310-16 Table for its wirings**

This table is for "Allowable Ampacities of Insulated Conductors Rated 0 Through 2000 Volts, 60°C Through 90°C (140°F Through 194°F), Not More Than
Three Current-Carrying Conductors in Raceway, Cable, or Earth (Directly Buried), Based on Ambient Temperature of 30°C (86°F)"

## Schematic

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/main/images/DriverAndMotorRevisionEight.jpg)

The schematic above shows the wiring connections between the microcontroller/microcomputer, driver, and motor. The resistor options for connecting the microcontroller/microcomputer with the driver are: 0 for 5V, 1kΩ for 12V, or 2kΩ for 24V. Because there are 5 resistor connections, 10, 2kΩ resistors would suffice for covering all of them, in which we can use 2, 2kΩ resistors in parallel to create a 1kΩ connection.

This selected dirver and motor will be able to connect and work together. The driver, STP-DRVAC-24025, states "Only use stepper motors wound for high bus voltages (**STP-MTRAC** motors) with high bus voltage drives (STP-DRVAC-xxxxx)." The motor we chose follows this naming convention: **STP-MTRAC**-34156.

Also to note, the STP-DRVAC-20425 driver can take a nominal input voltage of 90-240VAC. Because of this we will not need a step-down transformer.
^ Source: https://www.automationdirect.com/adc/shopping/catalog/motion_control/stepper_systems/stepper_drives/stp-drvac-24025
^ Source: https://www.automationdirect.com/adc/shopping/catalog/motion_control/stepper_systems/single_shaft_stepper_motors/stp-mtrac-34156

The fuses labeled in the schematic are AGC4 fuses. These are "Bussmann fuse, AGC series, small dimension, fast-acting, 4A, 250 VAC, glass tube." This protects the system for 160% of the rated current **and** are the manufacturer recommended fuses.

To adhere to the NEC 310-16 table, the following must be considered:

The datasheet states that the driver will draw 2.5 Amps per phase. Note that this does not mean that it will draw current equal to 2.5 times the number of phases. It simply means that every time the phase is changed, the driver will draw 2.5 Amps.

Because we are getting rid of the transformer, there will be no primary and secondary windings to account for, and there will only be 1 set of wires connecting the wall outlet to the driver. No power analysis is needed because we already know the input voltage and the draw current.

This means the wires must be able to withstand 2.5A.

14 gauge, TW (Or Thermoplastic high-heat resistance and water-resistant) copper wires will suffice for the wires as according to the table, at 140°F, they can withstand a max of 20 Amps. This is well above our expected current draw for the driver.

Based on the table for wire resistances, the DC resistance of 14 gauge, TW, solid copper wiring at 167°F is 3.070Ω per 1000 feet of wiring. We will not use this much wiring.

Assuming we use **at max** 10 feet if wiring, the power losses will be

$L = (I^2)(R)(10/1000)$
$L = (2.5^2)(3.070)(0.01) = 0.1919W$

The losses over the total power of this system will be

$(L/W)(100) = (0.1919/300)(100) = 0.064

This loss is 0.064%. This loss will be minimal, and the transformer will suffice for maintaining the power output we need.

^ Source: https://www.automationdirect.com/adc/shopping/catalog/motion_control/stepper_systems/stepper_drives/stp-drvac-24025
^ Source: https://media.distributordatasolutions.com/ThomasAndBetts/v2/part2/files/File_7437_emAlbumalbumsOcal20(USA)oc_1_g_nec31016pdfClickHerea.pdf
^ Source: https://www.lincenergysystems.com/blog/difference-between-tracer-wire-tw-thw-thhn/
^ Source: http://www.paigewire.com/wire_resistance-prop.aspx?AspxAutoDetectCookieSupport=1

![MotorMount](https://github.com/DillonSW/Capstone_Team_5/blob/main/images/MotorMount.jpg)

The image above shows the proposed idea of mounting the motor into the machine. Proposed by the Mechanical Engineering team, the motor will be mounted at the bottom of the machine, and will be on the same level as the mount for the platforms.

![Connection](https://github.com/DillonSW/Capstone_Team_5/blob/main/images/PulleySystem.jpg)

The image above shows the proposed idea of having the motor rotate the platforms. Proposed and discussed by the Mechanical and ECE teams, there will be a gear or belt-feed attatched to the motor's shaft and to the platform's base. These mounts will be of identical size in order to keep the ratio of motor rotation and platform rotation equal. Of course, there will be efficiency loss; any belt-feed or gear ratio will have some sort of loss. As shown in the calculations, we are assuming the worst-case scenario of 50% efficiency.

## Analysis

As stated previously, the motor must be able to output enough torque to rotate roughly 75 lbs. Our current machine design is a hollow cylinder, with the outer diameter being 3' and the inner, hollow diameter being roughly 1'4" 

Below is some algebra that help derive the correct formula to use for our system:

$T = Torque$ | 
$I = Moment of Inertia$ | 
$α = Angular Acceleration$ | 
$a = Acceleration$ | 
$r = Radius$ | 
$m = Mass$

Torque is usually found by multiplying Force and the Radius of the cylinder.

$T = Fr$

Force is equal to mass x acceleration 

$F = ma$

By reorganizing  

$a = F/m$                (1) 

Acceleration can also be expressed as 

$a = (d/dt)(ds/dt)$

For rotatory motion $s = rdθ$

$a = (d/dt)(rdθ/dt)$

Reorganize 

$a = r(d/dt)(dθ/dt)$

Angular Acceleration (α) 

$α = (d/dt)(dθ/dt)$

This means α can be substituted in 

$a = rα$                 (2)

The formula for torque can be reorganized in to 

$F = T/r$                (3)

By substituting equations (2) and (3) into (1), we get 

$rα= (T/r)/m$

Which can be reorganized in to 

$T=mr^2α$

The formula for moment of inertia is 

$I = mr^2$ 

Which can be substituted in as 

$T= Iα$  

Confirming the equation needed to be used to find our Torque.
Since we are working with a cylinder with a hollow center, we are using the equation required to find the moment of inertia for an Annular cylinder

$I= (1/2)M(R1^2+R2^2)$

This equation has been confirmed by multiple sources, and fits into the standards for the equation for moment of inertia

$I = mr^2$ 

$T=W(R1^2+R2^2)/2∗(∆N/308t)$

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
^ Source further explaining equation: https://www.powertransmission.com/ext/resources/issues/0417/baldor-basics.pdf?1646351827

The values of W, R1, & R2 Are consistence since they are the current constraints of our design:  
W = 85 lb 

R1 = 1.5 ft 

R2 = 0.667 ft 

While the values of ∆N & t will vary for testing purposes: 
∆N1 = 5 rpm 

**∆N2 = 3 rpm** 

∆N2 = 1 rpm 

t1 = 0.25 sec 

**t2 = 0.5 sec** 

t2 = 1 sec  

Our current goal is for the rotary device to take roughly 3 seconds to transition from 1 compartment to another. The device would need to rotate 18° to have a complete transition. Luckily for us our choice of stepper motor makes it so each step is 1.8°, which makes it so we have to take exactly 10 steps to reach the next compartment. Using this information, we can determine that are desired rpm will be roughly 1 rpm since 18°/3 sec =6° per second.  

To find the motor that would work best for our project  

Stepper Motors are DC motors that divided a full rotation into a set of equal steps. This will give us greater control on speed and movement of our motor, and the math happens to work in our favor.  

To know what type of stepper motor we need, we have to calculate the torque it will need to properly rotate our device.  

With the known values above, and the values that can be varied, a torque calculation table can be created for each case:  

**Givens:**  
W = 85 lbs  
R1 = 1.5 ft  
R2 = 0.67 ft  

**Required Torque Calculations (lb-ft)**  

|  t(s)  |        |∆N (rpm)|        |  
|--------|--------|--------|--------|
|        |    1   |    2   |    3   |
|  0.25  | 1.4872 | 4.4616 | 7.4360 |
|  0.5   | 0.7436 | 2.2308 | 3.7180 |
|    1   | 0.3718 | 1.1154 | 1.8590 |  

**Converted to Nm**  

|  t(s)  |        |∆N (rpm)|        |  
|--------|--------|--------|--------|
|        |    1   |    2   |    3   |
|  0.25  | 2.0164 | 6.0491 | 10.0818 |
|  0.5   | 1.0082 | 3.0245 | 5.0409 |
|    1   | 0.5041 | 1.5123 | 2.5205 |  

As shown above, the highest amount of torque required would be at 5 rpm, accelerating in 0.25 seconds. This torque would be 10.0818 Nm.  
However, these results are assuming that a DC motor will be 100% efficient when operating at a lower rated load. This is an unreasonable expectation. Most DC motors are designed to be anywhere from 50-100% efficient with peak efficiency being at around 75% of the rated load. So for a 13 Nm motor, the optimal load range is from 6.5 to 13 Nm, with peak being at 9.25 Nm. Because we would have at most 10.0818 Nm of required torque, and an assumed efficiency of 50% the most torque requited would be 20.1636 Nm. However we are deciding to run the motor assuming a lower acceleration time and rpm. At the values we are expecting to run (0.5s acceleration and 3 rpm), also assuming 50% efficiency, the required torque would be 6.049 Nm, which is close to the acceptable level for our desired motor. 

^ Source: https://www.energy.gov/sites/prod/files/2014/04/f15/10097517.pdf 

A safety measure we must take into account is the potential for a pinch point to occur. According to OSHA 1910.211(d)(44)
* Pinch point means any point other than the point of operation at which it is possible for a part of the body to be caught between the moving parts of a press or auxiliary equipment, or between moving and stationary parts of a press or auxiliary equipment or between the material and moving part or parts of the press or auxiliary equipment. 

^ Source: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.211 

Due to this definition, a pinch point can occur between the dividers and the frame of the machine during platform rotation. This is why we are leaving a 1 in. gap between the platforms and the frame. 

We will assume that the radius from the frame to the pulley / gear is 1.2 ft (or 0.36924 m). 

Given the average width of an index finger is 0.75 in.: 

$T = Fr$

$6.049 = F(0.36924)$ -> $F = 16.3823 N = 3.68289 lb$

We are going to assume that the force acting on a finger in the pinch point will act like shear-force.

The equation for shear-force is: 

$τ = F/A$ 

Where 
$τ = Shear Force$ |  
$F = Force Applied$ | 
$A = Cross-sectional Area, parallel to F$

^ Source: https://www.engineersedge.com/material_science/shear-stress.htm 

For a 1 in. long gap, with an average .75 in. width finger, 

$A = (length)(width) = 0.75 in^2$

So 

$τ = 3.68289/0.75 = 4.91052 lb/in^2$

The max applied shear force on a finger in the given scenario is roughly 5 lb/in^2. This is also assuming that the finger cannot bend. The force required to fracture a "small bone" can be as little as 25 lbs of pressure. It is safe to assume that 1/5th of the minimum force required to fracture a small bone will not cause severe damage. This can be tested by using an object similar to a finger (such as a baby carrot) and rotating the platforms while the carrot is in the door. 
^ Source: https://scienceline.ucsb.edu/getkey.php?key=3088 

If all else fails, there can be a delay for the platform rotating. During this delay, the user interface can display a message to remove any appendages from the machine, or it can be pinched. There can also be a sign attached to the machine. 

**Note**
The torque required to stop the device is well below the holding torque of the selected motor. Also, since this motor has an electromagnetic brake, it will have even greater stopping power assuring the motor does not lose its step. A table displaying the pull out torque is placed below. Pull Out Torque is the maximum torque the brake can output at higher speeds. The higher the rmp, the less it can brake. Our maximum speed (5 rpm) will not come close to being an issue.  
![PulloutTorque](https://github.com/DillonSW/Capstone_Team_5/blob/main/images/NewMotorTorque.jpg)

Since the motor we are looking at can have a holding torque of 9 Nm at 5 rps, a higher speed than we intend to run the motor, it will meet the constraints of outputting enough torque and securing the devices. We would be able to operate the motor at a lower demand than its maximum, putting less strain on the motor over time.  

The motor, as stated before, can rotate 1.8° per step. The datasheet does not directly state tolerances for the step angle. However, compared to our previous motor selection, this motor is considerably more expensive. It can be assumed that the precision may be equal, meaning that there is a 0.09 tolerance, meaning the motor can step anywhere from 17.1° to 18.9° in 10 steps. Because the Mechanical Engineering team plans on keeping the rotation ratio between the motor and the platform the same, there will be, at maximum, 0.9° of error per board. This error is allowable, as this is not enough error for the sensor to miss the board during a rotation.

The datasheet gives different amounts of micro steps that the encoder can have. These values can range from 200 to 25600. An encoder's resolution can be represented as pulses per revolution (PPR). Given that the stepper motor we chose has can rotate 1.8° per step, the minimum PPR we would need is

$N = 360/I$

Where

N = Number of points per revolution (or per 360°)

I = Smallest required increment of measurement. For this motor, $I = 1.8°$

Therefore

$N = 360/1.8 = 200$

This means that the bare minimum amount of PPR, or encoder resolution, that we would need to accurately reach our destination is 200. Because the stepper motor driver encoder's resolution can go from 200 to 25600, and resolution will suffice for precisely meeting our specifications. To account for potential error and to further increase the precision and accuracy of our stepper motor, we will choose an encoder resolution of 12800 PPR.

## BOM

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| STP-MTRAC-34156 | Stepper Motor for Rotating Platforms | Motor | STP-MTRAC-34156 | SureStep | 1 | $284.00 | $284.00 |
| STP-DRVAC-24025 | AC Microstepping Stepper Driver | Motor | STP-DRVAC-24025 | SureStep | 1 | $213.00 | 213.00 |
| 10A DIN Rail Circuit Breaker | 1 Pole, 10 Amp, 230/400V AC | Motor | CADZ47-63-C10-1P | Smseace | 2 | $8.99 | $17.98 |
| JOS 2 kΩ Resistor | 5% Tolerance, Carbon film, 1/4 Watt | Motor | 10EP5142K00  | E_Projects | 10 | $0.573 | $5.73 |
| FAZ-D4-1-SP | Single Pole, 4 Amp, DIN Rail Mount Breaker | Motor | FAZ-D4-1-SP | Eaton | 2 | $15.00 | $30.00 |
| **Total** |  |  |  | **Total Components** | 16 | **Total Cost** | $550.31 |

