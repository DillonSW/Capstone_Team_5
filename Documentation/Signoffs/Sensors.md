# Sensors System

## Subsystem Function 

The role of the sensor subsystem is to send signals, communicating the occupancy of the presently forefront compartment sections, to the PLC to update certain tags, so that the PLC's ladder logic code can properly use that information ad hoc.  

 

Constraints 

 

The Sensors: 

* **Must identify whether a device is present or if it is not.**  

* **Cannot take up too many I/O pins in the PLC**   

    ^The PLC module will have a limited amount of inputs and outputs to receive or send signals.  

* **Must be of suitable size.**  
 
    ^They have to fit in the proper place in the vending machine 

 

## Schematic 
![SensorSchematic](https://user-images.githubusercontent.com/113734069/203670775-6f40ee67-78c1-44de-b468-94481cb20bdc.jpeg)

This is how to Time of flight sensor is going to work. We have designated three I/O pins—7, 8, and 9—of our PLC module to input signals from our sensors. 

 
## Analysis 

There are hundreds of different sensor options to choose from, so it took much deliberation to choose the right one. Most options were easy to disregard through common sense, like for sensors that would obviously be too expensive or too large for the scale of our project. The main sensors considered included Weighing Sensors, Pressure Sensors, Ultrasonic sensors, and Photoelectric sensors. 

 

**Weighing Sensor:**   

These sensors are scales that measure the weight based on the force applied from whatever is on top of them. These could be placed under each compartment to measure the weight and to send that data to the PLC to determine if the measured weight indicates that there is a device in the compartment. This sensor is not ideal because the data it sends is not a one-bit signal; multi-bit signals would require more complicated ladder logic code and I/O pins. Also there is risk of these weighing scales needing recalibration after the vending machine being moved. 

 

**Pressure Sensors:**   

These sensors, unlike the weighing sensors, send a one bit signal once any force is applied from the weight of an object above the sensor. To implement these sensors however we would need one in every compartment of our vending machine which would be around sixty that we would need to wire, power, and connect to the PLC—this is not feasible. 

 

**Ultrasonic Sensors:**   

These sensors transmit waves and receive them once these waves are reflected back off an object in front of them. The time it takes to receive the wave is then use to calculate the distance of the object in front of the sensor. With these sensors we would only need three of them: one for each of the three levels of the dial. The sensor would be positioned inside under each door of the dial; it would be pointed towards the compartment that is currently rotated to be behind the door. The problem with these sensors is that they don't send a one bit signal just like the weighing sensor. 

 

**Photo-Eye Sensor:**   

This sensor is a photoelectric sensor that emits an infrared light beam across to a mirror that reflects it back to the sensor. If something obstructs the path of the beam then the sensor knows that there is an object in front of it because the infrared beam is not returned. What is ideal about these sensors is that we would only need three of them too, and they could be positioned just as the location of the ultrasonic sensors were described. However, there would have to be sixty mirrors on the back side of every compartment to reflect the infrared beam back to the photo-eye sensor. 

 

**Spot Sensors:**   

This sensor is just like the photo-eye sensor being a photoelectric sensor, but the difference is that the spot sensor is a diffuse reflection sensor which means this sensor does not need mirrors to reflect the light back. The spot sensor also has background suppression; It can be calibrated to only sense up to a certain distance. With this function we could adjust the calibration to where it would not take in light reflected from the back wall of the compartment, but the sensor would still sense a closer object that could be there. The following figures illustrates this where: 

A = Sensor 

B = Object 

C = Background 

X = Distance between object and sensor 

X + Y = Distance between sensor and background 

 ![Object_Background_Suppression](https://user-images.githubusercontent.com/113734069/203670906-74718655-fcee-4934-bc84-a7e235f93afe.jpeg)

SP1 = Set Max Sensing Distance 

![Background_Suppression](https://user-images.githubusercontent.com/113734069/203670924-26edff27-894f-49f0-8af1-3afa87baff16.jpg)
 
We have identified the photoelectric diffuse reflection spot sensor with background suppression to be the most ideal sensor to use for our vending machine sensor system. In particular we have chosen to use the ifm OGH580; this sensor has an operating voltage of 10-30V DC and has a sensing range of up to 200mm. If placed out of but pointing at the compartment inside the vending machine, this sensor should be sufficient in identifying whether a device is present or not. This sensor is also certainly of suitable size to fit inside of the vending machine; it would not pose an obstacle to stocking or obtaining a device from the compartment. Lastly, because we will only be using three one-bit signal sensors, we will only have to allocate three I/O pins of the PLC module for our sensor system.  

 
## BOM 

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total | 
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------| 
| OGH580 | Diffuse Reflection sensor with background suppression | Sensors |OGH-FPKG/US/CUBE  | ifm Efector inc. | 3 | $87.12 | $261.36| 
| **Total** |  |  |  | **Total Components** | 3 | **Total Cost** | $261.36 | 
