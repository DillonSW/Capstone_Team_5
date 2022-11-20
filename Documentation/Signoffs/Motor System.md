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

* **Will have a time to accelerate (the loads) of less than 1 second.**
^ As explained below, we want our time to accelerate to be 0.5 seconds. We can run our calculations based off of 1 second time to accelerate as a worse-case scenario.

**Circuity:** 
* **Will be protected at 125% the nameplate current rating (7.5A).** This comes from the following codes.

The standard NEC 430.52(D) states "Torque motor branch circuits shall be protected at the motor nameplace current rating in accordance with 240.4(B)

^ Source: https://up.codes/s/rating-or-setting-for-individual-motor-circuit

NEC 240.4(B) is the standard for overcurrent devices rated 800 amperes or less, which allows the use of a higher rated overcurrent device as long as the conditions are met. All of these conditions have been cleared.  
 * The conductors being protected are not part of a branch circuit supplying more than one receptacle for cord-and-plug-connected portable loads.  
 * The ampacity of the conductors does not correspond with the standard ampere rating of a fuse or a circuit breaker without overload trip adjustments above its rating (but that shall be permitted to have other trip or rating adjustments).  
 * The next higher standard rating selected does not exceed 800 amperes.  
^ Source: https://up.codes/viewer/illinois/nfpa-70-2020/chapter/2/wiring-and-protection#240.4_(B)  

The standard NEC 705.12(D)(2) Bus or Conductor Ampere Rating states "One hundred twenty-five percent [125%] of the inverter output circuit current shall be used in ampacity calculations for the following: Feeders, Taps, and Busbars."

^ Source: https://up.codes/viewer/delaware/nfpa-70-2014/chapter/7/special-conditions#705.12_(D)_(2)

## Schematic

<img src="https://github.com/DillonSW/Capstone_Team_5/blob/main/images/Driver and Motor Schematic.jpg" width=50% height=50%>
The schematic above shows the wiring connections between the microcontroller/microcomputer, driver, and motor. The resistor options for connecting the microcontroller/microcomputer with the driver are: 0 for 5V, 1kΩ for 12V, or 2kΩ for 24V. Because there are 5 resistor connections, 10, 2kΩ resistors would suffice for covering all of them, in which we can use 2, 2kΩ resistors in parallel to create a 1kΩ connection.

## Analysis

As stated previously, the motor must be able to output enough torque to rotate roughly 75 lbs. Our current machine design is a hollow cylinder, with the outer diameter being 3' and the inner, hollow diameter being roughly 1'4" 

Below is some algebra that help derive the correct formula to use for our system:

$T = Torque$
$I = Moment of Inertia$ 
$α = Angular Acceleration$ 
$a = Acceleration$ 
$r = Radius$ 
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
However, these results are assuming that a DC motor will be 100% efficient when operating at a lower rated load. This is an unreasonable expectation. Most DC motors are designed to be anywhere from 50-100% efficient with peak efficiency being at around 75% of the rated load. So for a 12 Nm motor, the optimal load range is from 6 to 12 Nm, with peak being at 9 Nm. Because we would have at most 10.0818 Nm of required torque, and an assumed efficiency of 50% the most torque requited would be 20.1636 Nm. However we are deciding to run the motor assuming a lower acceleration time and rpm. At the values we are expecting to run (0.5s acceleration and 3 rpm), also assuming 50% efficiency, the required torque would be 6.049 Nm, which is an acceptable level for our desired motor. 

^ Source: https://www.energy.gov/sites/prod/files/2014/04/f15/10097517.pdf 

**Note**
The torque required to stop the device is well below the holding torque of the selected motor. Also, since this motor has an electromagnetic brake, it will have even greater stopping power assuring the motor does not lose its step. A table displaying the pull out torque is placed below. Pull Out Torque is the maximum torque the brake can output at higher speeds. The higher the rmp, the less it can brake. Our maximum speed (5 rpm) will not come close to being an issue.  

<img src="https://github.com/DillonSW/Capstone_Team_5/blob/main/images/PulloutTorque.jpg" width=50% height=50%>

Since the motor we are looking at can have a holding torque of 12 Nm, it will meet the constraints of outputting enough torque and securing the devices. We would be able to operate the motor at a lower demand than its maximum, putting less strain on the motor over time.  

## BOM

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
| P Series Nema 34 Stepper Motor | Stepper Motor for Rotating Platforms | Motor | 34E1KBK50-120 | Stepper Online | 1 | $195.01 | $195.01 |
| HSS86        | Hybrid Stepper Servo Driver | Motor | NBKDM-HBS86H | MEIHAOCNC | 1 | $55.00 | $55.00 |
| JOS 2 kΩ Resistor | 5% Tolerance, Carbon film, 1/4 Watt | Motor | 10EP5142K00  | E_Projects | 10 | $0.573 | $5.73 |
| **Total** |  |  |  | **Total Components** | 12 | **Total Cost** | $255.74 |

