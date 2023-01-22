# Identification Subsystem  

## Subsystem Function  

This Subsystem's role in the team's design is to scan barcodes on school devices before being placed and when being taken from the machine. The subsystem also includes a RFID Card Reader to verify and store students' identity. The PC will then receive information from the modules and store information in a database for our customer. 

## Constraints  

* Barcode Scanners shall be low power and consume no greater than 5 V 0.5 A. This is due to being powered by the miniPC. Common computers only output a max rating of 5 V 0.5 A.  
^ Source: https://resources.pcb.cadence.com/blog/2020-what-are-the-maximum-power-output-and-data-transfer-rates-for-the-usb-standards  

* Barcode Scanners shall be able to decode Code-128 barcodes 

* RFID Card Scanner shall be low power and consume no greater than 5 V 0.5 A   

* RFID Card Scanner shall operate on 13.56 MHz commonly used for higher security access badges  

* Barcode Scanners and the RFID Card reader shall be powered by a USB port to communicate with the miniPC  

* A Barcode Scanner and Card Reader will be monitered by USB voltmeter to ensure correct operation  

* Barcodes shall be of decent quality to follow ISO 15416 standard. Assures that the codes can be read by any scanner  

* The MiniPC shall run on Windows to provide the needed applications for PLC and Database

* The MiniPC shall occupy no larger than a 6x6 in. space to fit in the machine

* The MiniPC will provide an ethernet port to communicate with the PLC

* Shall include a USB Hub to provide enough ports for modules

## Schematic  

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-signoff-Barcode-Scanner/images/ID_System.jpg?raw=true)  

The Schematic above shows the layout of the ID subsystem 

## Analysis  

Commonly a barcode scanner is made up of three parts: illumination system, sensor system, and decoder. The illumination system is responsible for emiting a red light onto the code which seperates the dark and light sections. The sensor detects the reflected light from the white portion of the code and generates an analog signal which is then sent to the decoder. The decoder will translate the signal into text and checks the information with the check digit. The text is then finally sent to the computer connected to the device to be read.  

^ Source: https://www.waspbarcode.com/buzz/how-barcode-scanners-work  

RFID systems are made up of an antenna, transceiver, and a transponder. In a reader, the transceiver and transponder are combined. The reader emits a radio signal which is received by the card. The card then responds with its signal which is read by the reader. RFID tags fall into an active and passive category. The ID card held by students is powered by the signal from the reader, so it falls into the passive category. Passive tags can usually only transmit as far as 4 inches. The tag normally holds less than 2000 KB of data. The card held by students at Tennessee Tech University holds 253 bytes. The most common RFID systems are LF (125 kHz) and HF (13.56 MHz). Normally, security cards are on the HF system.  

^ Source: https://www.techtarget.com/iotagenda/definition/RFID-radio-frequency-identification#:~:text=The%20RFID%20reader%20is%20a,in%20the%20RFID%20tag%20itself.

To verify correct operation of the barcode scanner and the RFID reader, a USB voltmeter will be used connecting the scanners to the PC. This will allow the team to monitor the scanner during operation and ensure the 5 V 0.5 A limit is not exceeded, and the scanners operate at the correct standby current. The Barcode scanner shall be a 2D barcode scanner that is able to decode both 1D and 2D codes. The code the team is using is a 1D Code-128 barcode since they are easy to design and will be cheap to order for the devices.  

The current USB voltmeter in mind is the 2 in 1 USB micro and type C connector and the scanner is the Waveshare USB scanner module that will work along the PC.  
The voltmeter is able to monitor the Voltage and Current taken by the Module. A benefit of the meter is the ability to verify operating current and voltage when a box is scanned.  

The scanner will be used at different ranges to determine an appropriate range for a box to be placed and still be correctly read. To verify the code information, the scanner output will be compared with the expected outcome to ensure a box is not mislabeled. There will be 2 barcode scanners. One will be placed inside the machine so boxes can be loaded. Another will be outside the machine with the RFID reader to scan when a student gets a box. All the modules will be fed through a usb hub.  

To remove data from the computer for use, a program will be added to the MiniPC so when the drive is plugged in, the information is downloaded automatically. The port will be behind a locked compartment so students cannot access the data.  

## BOM  

| Name of item | Description | Subsystem | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|--------------|----------|-------|-------|
| Eversame 2 in 1 USB Tester | Voltmeter | Identification System | Eversame | 2 | $22.99 | $45.98 |  
| Barcode Scanner Module | 1D/2D Code Reader | Identification System | Waveshare | 2 | $39.99 | $79.98 |  
| RFID Reader | 13.56 MHz card reader | Identification System | Vipxyc | 1 | $14.99 | $14.99 |  
| USB Hub | 7-port | Identification System | IVETTO | 1 | $29.99 | $29.99 | 
| MiniPC | Windows 10 Pro | Identification System | ATOPNUC | 1 | $129.99 | $129.99 | 
|  |  |  | **Components** | 7 | **Total Cost** | $300.93 |  
