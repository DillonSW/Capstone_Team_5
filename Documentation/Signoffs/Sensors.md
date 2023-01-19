# Sensors System 

  

## Subsystem Function  

  

The role of the sensor subsystem is to send signals—communicating the status of the device occupancy of the presently forefront compartment sections on all three dial layers—to the PLC to update certain tags, so that the PLC's ladder logic code can properly use that information ad hoc.   

  

 

## Constraints  

  

**The Sensor System:** 

   

* **Cannot take up more than three I/O pins from the PLC**    

   ^The PLC module will have a limited amount of inputs and outputs to receive or send signals. All other pins will need to be allocated to receive from and or send signals to the locks, LEDs, and motor.  

   ^This also makes the constraint that the sensors must send one bit signals since there will have to be three separate —one for each dial layer (which each take up one I/O pin). 

 

* **Must send a zero signal to the PLC if there is a device in the presently forefront compartment section and a one signal if there is not.**  

   ^ The signal may be inverted as well; the signal just needs to be able to properly communicate the state of the compartment to the ladder logic code of the PLC. 

 

* **Have a type of sensor that is capable of identifying whether a compartment is empty or not, communicate that information through a one bit signal, and not obstruct access to the compartment.** 

   ^To specify the last part of the constraint the sensor must fit inside the palm of your hand—this should be sufficiently small and practically achievable. 

 

  

## Schematic  

![SensorSchematic](https://user-images.githubusercontent.com/113734069/203670775-6f40ee67-78c1-44de-b468-94481cb20bdc.jpeg) 

  

We have designated three I/O pins—7, 8, and 9—of our PLC module to input signals from our sensors.  

  

  

## Analysis  

  

There are hundreds of different sensor options to choose from, so we deliberated extensively to choose the best sensor for our purposes. Through common sense, most options were easy to disregard—like sensors that would obviously be too expensive or too physically large for the scale of our project. The main sensor considerations included Weighing Sensors, Pressure Sensors, Ultrasonic sensors, and Photoelectric sensors.  

  

**Weighing Sensor:**    

These sensors are scales that measure the weight based on the force applied from whatever is on top of them. These could be placed under each compartment to measure the weight and to send that data to the PLC to determine if the measured weight indicates that there is a device in the compartment. This sensor is not ideal because the data it sends is not a one-bit signal; multi-bit signals would require more complicated ladder logic code and I/O pins. Also there is risk of these weighing scales needing recalibration after the vending machine being moved. 

  

**Pressure Sensors:**    

These sensors, unlike the weighing sensors, send a one bit signal when any force is applied from the weight of an object above the sensor. To implement these sensors however we would need one in every compartment of our vending machine which would be around sixty that we would need to wire, power, and connect to the PLC—this is not feasible.  

  

**Ultrasonic Sensors:**    

These sensors transmit waves and receive them when these waves are reflected back off an object in front of them. The time it takes to receive the wave is then use to calculate the distance of the object in front of the sensor. With these sensors we would only need three of them: one for each of the three levels of the dial. The sensor would be positioned inside under each door of the dial; it would be pointed towards the compartment that is currently rotated to be behind the door. The problem with these sensors is that they don't send a one bit signal just like the weighing sensor.  

  

**Photo-Eye Sensor:**    

This sensor is a photoelectric sensor that emits an infrared light beam across to a mirror that reflects it back to the sensor. If something obstructs the path of the beam then the sensor knows that there is an object in front of it because the infrared beam is not returned. What is ideal about these sensors is that we would only need three of them too, and they could be positioned just as the location of the ultrasonic sensors were described. However, there would have to be sixty mirrors on the back side of every compartment to reflect the infrared beam back to the photo-eye sensor.  

  

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

  

We have identified the photoelectric diffuse reflection spot sensor with background suppression to be the most ideal sensor to use for our vending machine sensor system. In particular we have chosen to use the ifm OGH580; this sensor has an operating voltage of 10-30V DC and has a sensing range of up to 200mm—This range is sufficient for covering the distance between the device in the compartment and the sensor. If placed out of but pointing at the compartment inside the vending machine, this sensor should be sufficient in identifying whether a device is present or not. This sensor is also certainly of suitable size to fit inside of the vending machine; it would not pose an obstacle to stocking or obtaining a device from the compartment. Lastly, because we will only be using three one-bit signal sensors, we will only have to allocate three I/O pins of the PLC module for our sensor system.   

The sensors will be able to be grounded, be powered, and send signals through female end cord sets connecting the sensors to the power supply, PLC, and ground bar. The ifm EVC001 is a two meter long cord that is made to work with this spot sensor. Two meters is of sufficient length to connect all of our sensors to ground and each of these systems. Inside the cable jacket of this cord are four wires: a ground, neutral, power, and signal wire. The power wires will be connected to three terminal blocks that are jumped together and connected to the power supply high side. The neutral and ground wires will be connected to six terminal blocks that are jumped together and connected to ground. The signal wires will be connected straight to the 7, 8, and 9 I/O pins of the PLC.

  

## BOM  

  

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |  

|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|  

| OGH580 | Diffuse Reflection sensor with background suppression | Sensors |OGH-FPKG/US/CUBE  | ifm Efector inc. | 3 | $87.12 | $261.36|  

| EVC001 | Female Cord set | Sensors | ADOGH040MSS0002H04 | ifm Efector inc | 3 | $11.50 | $34.50 | 

| **Total** |  |  |  | **Total Components** | 6 | **Total Cost** | $295.86 |  
