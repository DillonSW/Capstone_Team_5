# Sensors System 

  

## Subsystem Function  

  

The role of the sensor subsystem is to send signals—communicating the status of the device occupancy of the presently forefront compartment sections on all three dial layers—to the PLC to update certain tags, so that the PLC's ladder logic code can properly use that information ad hoc.   

  

 

## Constraints  

  

**The Sensor System:** 

   

* **Cannot take up more than three I/O pins from the PLC**    

   ^The PLC module will have a limited amount of inputs and outputs to receive or send signals. All other pins will need to be allocated to receive from and or send signals to the locks, LEDs, and motor.  

   ^This also makes the constraint that the sensors must send one bit signals since there will have to be three separate—one for each dial layer (which each take up one I/O pin). 

 

* **The distance sensor chosen must determine the presence or absence of a device by measuring whether the light emitted was reflected back from a distance shorter than the distance between the sensor and the back wall of the compartment.** 

   ^To understand why the sensor must be a light emitting distance sensor see the analysis section below. 

   ^The sensor must not communicate the presence of a device by sensing the back wall of the compartment. 

 

* **Must send a one signal to the PLC if there is a device in the presently forefront compartment section and a zero signal if there is not.**  

   ^This constraint is chosen when considering the consequences in the case of the wire being cut: 

If the default (zero) signal communicates that a device is present then the door could be able to be opened, upon someone trying to check a device out, because         the PLC thinks there is a device there to be distributed. 

If the default (zero) signal communicates that a device is not present then the door will remain locked and cannot be unlocked because the PLC thinks there is no       device there to distribute. 

Upon reflection the second option is the best because the devices are protected behind the locked door which will prevent theft during the time period before the       wire connection is fixed. 

 

* **The sensor should be small enough to fit inside the palm of your hand so as not to obstruct access to the compartment** 

   ^This should be sufficiently small and practically achievable to find a sensor of such size. 
 

  

## Schematic  

![SpotSensorsSchematic1](https://user-images.githubusercontent.com/113734069/215000045-7e4d8fe0-7820-4f14-8b34-5ba22decf83a.jpg)


We have designated three I/O pins—7, 8, and 9—of our PLC module to input signals from our sensors. Each of the three sensors has three wires; the signal wires (SDA) will be connected to their respective input pin of the PLC; the wires powering the sensors (AVDD) will be connected to terminal blocks--jumped together--to connect directly to the positive voltage wire of the power supply; the neutral wires of the sensors (NTRL) will also be connected to terminal blocks that are jumped together. As depicted in the diagram the top level, middle level, and bottom level sensor will be connected to pin 9, pin 8, and pin 7 of the PLC respectively. 

  

  

## Analysis  

  

There are hundreds of different sensor options to choose from, so we deliberated extensively to choose the best sensor for our purposes. Through common sense, most options were easy to disregard—like sensors that would obviously be too expensive or too physically large for the scale of our project. The main sensor considerations included Weighing Sensors, Pressure Sensors, Ultrasonic sensors, and Photoelectric sensors. The sensors we ultimately decided on using were Photoelectric time of flight spot sensors. 

  

**Spot Sensors:**     

  

This sensor is just like the photo-eye sensor, being a photoelectric sensor, but the difference is that the spot sensor is a diffuse reflection sensor which means this sensor does not need mirrors to reflect the light back. The spot sensor also has background suppression; It can be calibrated to only sense up to a certain distance. With this function we could adjust the calibration to where it would not take in light reflected from the back wall of the compartment, but the sensor would still sense a closer object that could be there. The following figures illustrates this where:   

  

A = Sensor  

  

B = Object  

  

C = Background  

  

X = Distance between object and sensor  

  

X + Y = Distance between sensor and background  

  

![Object_Background_Suppression](https://user-images.githubusercontent.com/113734069/203670906-74718655-fcee-4934-bc84-a7e235f93afe.jpeg) 

  

SP1 = Set Max Sensing Distance  

  

![Background_Suppression](https://user-images.githubusercontent.com/113734069/203670924-26edff27-894f-49f0-8af1-3afa87baff16.jpg) 

  

We have identified the photoelectric diffuse reflection spot sensor with background suppression to be the most ideal sensor to use for our vending machine sensor system. In particular we have chosen to use the ifm OGH580; this sensor has an operating voltage of 10-30V DC and has a sensing range of up to 200mm—This range is sufficient for covering the distance between the device in the compartment and the sensor. The length of the compartment is 292mm, but the device box is 200mm meaning that if the device box is pushed to the back wall of the compartment there will be 92mm of distance between it and the edge of the compartment of the dial. The sensor mount is positioned 8mm outside of the dial but inside of the door. This means that at most the device box will be at a distance half of the sensors maximum range (100mm). If placed out of and pointing at the compartment inside the vending machine, this sensor will be sufficient in identifying whether a device is present or not. The sensor will emit photons which will reflect off of a device or the back wall and return to the sensor. Based on the time of flight calculated distance the sensor will use that information to determine if a device is present in or absent from the compartment. The sensor will be set to send a one value through the signal wire to the PLC if there is a device presently sensed, and the sensor will send a zero value through the signal wire to the PLC if there is not a device currently present. 

 This sensor is also certainly of suitable size to fit inside of the vending machine; it would not pose an obstacle to stocking or obtaining a device from the compartment. On top of that, because we will only be using three one-bit signal sensors, we will only have to allocate three I/O pins of the PLC module for our sensor system. Lastly, the wiring of three sensors is practicably achievable opposed to having a sensor per each compartment.  


The sensors will be able to be powered and send signals through female-end cord sets connecting the sensors to the power supply and PLC. The ifm EVC001 is a two meter long cord that is made to work with this spot sensor. Two meters is of sufficient length to connect all of our sensors to both the PLC and power supply. Inside the cable jacket of this cord are three wires: a neutral, power, and signal wire. The power wires will be connected to three terminal blocks that are jumped together and connected to the power supply high side. The neutral wires will be connected to three terminal blocks that are jumped together and connected to the neutral wire of the power supply. The signal wires will be connected straight to the 7, 8, and 9 I/O pins of the PLC—see the schematic for exact layout. 

  

## BOM  

  

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |  

|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|  

| OGH580 | Diffuse Reflection sensor with background suppression | Sensors |OGH-FPKG/US/CUBE  | ifm Efector inc. | 3 | $87.12 | $261.36|  

| EVC001 | Female Cord set | Sensors | ADOGH040MSS0002H04 | ifm Efector inc | 3 | $11.50 | $34.50 | 

| **Total** |  |  |  | **Total Components** | 6 | **Total Cost** | $295.86 |  
