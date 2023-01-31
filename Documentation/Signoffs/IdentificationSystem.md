# Identification Subsystem  

## Subsystem Function  

This Subsystem's role in the team's design is to scan barcodes on school devices before being placed and when being taken from the machine. The subsystem also includes a RFID Card Reader to verify and store students' identity. The PC will then receive information from the modules and store information in a database for our customer. The Windows PC will also be able to control the visual components like LEDs through a PLC.

## Constraints  

* Barcode Scanners shall be low power and consume no greater than 5 V 0.5 A. This is due to being powered by the PC. Common computers only output a max rating of 5 V 0.5 A.  
^ Source: https://resources.pcb.cadence.com/blog/2020-what-are-the-maximum-power-output-and-data-transfer-rates-for-the-usb-standards  

* Barcode Scanners shall be able to decode Code-128 barcodes 

* RFID Card Scanner shall be low power and consume no greater than 5 V 0.5 A   

* RFID Card Scanner shall operate on 13.56 MHz commonly used for higher security access badges, like the school Eagle Cards  

* A Barcode Scanner and Card Reader will be monitered by USB voltmeter to ensure correct operation  

* Barcodes shall be of decent quality to follow ISO 15416 standard. Assures that the codes can be read by any scanner  

* The PC shall run on Windows 10 to provide the needed applications for PLC and Database

* The PC will provide an ethernet port to communicate with the PLC through a USB NIC (network interface card)  

* The PC will provide at minimum an Intel Core i5-8400H or stronger CPU and 16GB RAM to support PLC programs

## Schematic  

![Schematic](https://github.com/DillonSW/Capstone_Team_5/blob/Team5-signoff-Barcode-Scanner/images/ID_System.jpg?raw=true)    

The Schematic above shows the layout of the ID subsystem. The PC connects to the PLC through a USB NIC, which is a USB to ethernet adapter, and is powered by the power subsystem. A USB Hub is connected to the MiniPC and allows for more modules. Two USB Voltmeters are used for a Barcode Scanner and RFID Reader. The UI system is connected to the MiniPC through the Hub as well.  

## Analysis  

Commonly a barcode scanner is made up of three parts: illumination system, sensor system, and decoder. The illumination system is responsible for emiting a red light onto the code which seperates the dark and light sections. The sensor detects the reflected light from the white portion of the code and generates an analog signal which is then sent to the decoder. The decoder will translate the signal into text and checks the information with the check digit. The text is then finally sent to the computer connected to the device to be read.  

^ Source: https://www.waspbarcode.com/buzz/how-barcode-scanners-work  

RFID systems are made up of an antenna, transceiver, and a transponder. In a reader, the transceiver and transponder are combined. The reader emits a radio signal which is received by the card. The card then responds with its signal which is read by the reader. RFID tags fall into an active and passive category. The ID card held by students is powered by the signal from the reader, so it falls into the passive category. Passive tags can usually only transmit as far as 4 inches. The tag normally holds less than 2000 KB of data. The card held by students at Tennessee Tech University holds 253 bytes. The most common RFID systems are LF (125 kHz) and HF (13.56 MHz). Normally, security cards are on the HF system.  

^ Source: https://www.techtarget.com/iotagenda/definition/RFID-radio-frequency-identification#:~:text=The%20RFID%20reader%20is%20a,in%20the%20RFID%20tag%20itself.

To verify correct operation of the barcode scanner and the RFID reader, a USB voltmeter will be used connecting the scanners to the PC. This will allow the team to monitor the scanner during operation and ensure the 5 V 0.5 A limit is not exceeded, and the scanners operate at the correct standby current. The Barcode scanner shall be a 2D barcode scanner that is able to decode both 1D and 2D codes. The code the team is using is a 1D Code-128 barcode since they are easy to design and will be cheap to order for the devices.  

The current USB voltmeter in mind is the 2 in 1 USB micro and type C connector and the scanner is the Waveshare USB scanner module that will work along the PC.  
The voltmeter is able to monitor the Voltage and Current taken by the Module. A benefit of the meter is the ability to verify operating current and voltage when a box is scanned.  

The scanner will be used at different ranges to determine an appropriate range for a box to be placed and still be correctly read. To verify the code information, the scanner output will be compared with the expected outcome to ensure a box is not mislabeled. There will be 2 barcode scanners. One will be placed inside the machine so boxes can be loaded. Another will be outside the machine with the RFID reader to scan when a student gets a box. All the modules will be fed through a usb hub.  

To remove data from the computer for use, a program will be added to the PC so when the drive is plugged in, the information is downloaded automatically. The port will be behind a locked compartment so students cannot access the data.  

To connect the Computer to the PLC, a USB NIC will be needed to provide an extra Ethernet port. The PLC uses Profinet, which is a communication protocol used to collect information and control a PLC through Profibus. The Computer will use an application called TIA Portal which allows connection and communication with the PLC and functions as a controller for S7 1200 and 1500 series PLCs. To use the TIA portal software, the PLC needs a minimum of 16 GB of RAM and an Intel Core i5-8400H or stronger CPU. The ThinkCentre provides enough RAM and a strong enough CPU to handle the program. The program will be created in the TIA portal and loaded to the memory on the PLC. TIA portal also provides diagnostics of the PLC through the software. The PLC the team is using is called a SIMATIC S7 1200 from Siemens and requires certain types of memory card. The three options of memory for the PLC differ only by capacity. The three options for memory size are 2, 4, and 24 MB. The team is using a 4MB memory card for the PLC since the 2MB is out of production. Issues have arrived with a USB NIC not being recognized by TIA Portal. If the software does not recognize the NIC, the way to fix the issue is to enter the IP address manually. The TIA Portal SIMATIC Step 7 program allows the use of an OPC UA Server.

^ Source: https://us.profinet.com/profinet-explained/, https://support.industry.siemens.com/cs/document/109784439/delivery-release-simatic-step-7-professional-basic-v17?dti=0&lc=en-WW  

To retain information from the PLC and PC, an OPC UA client from Prosys will be used. The OPC client allows the PLC to connect and send/receive data to a database. The database will be accessible to the PC as well. The database will be the interface between the PC and PLC. The PC will be able to set bits high to activate the PLC, and the PLC will be able to set the bits low after completion of the job. The OPC client is designed to be used with SIMATIC S7 1200 and 1500 series PLCs, and connect to the MySQL database software. The Prosys OPC client can connect directly to the Server created in the TIA portal software and then relay the information to the database for use by the PC and vice versa.  

^ Source: https://downloads.prosysopc.com/opcua/apps/JavaClient/dist/3.2.0-328/Prosys_OPC_UA_Client_UserManual.pdf  

## BOM  

| Name of item | Description | Subsystem | Manufacturer/Part# | Quantity | Price | Total |
|--------------|-------------|-----------|--------------|----------|-------|-------|
| Eversame 2 in 1 USB Tester | Voltmeter | Identification System | Eversame | 2 | $22.99 | $45.98 |  
| Barcode Scanner Module | 1D/2D Code Reader | Identification System | Waveshare | 2 | $39.99 | $79.98 |  
| RFID Reader | 13.56 MHz card reader | Identification System | Vipxyc | 1 | $14.99 | $14.99 |  
| ThinkCentre | Windows 10 Pro | Identification System | Lenovo | 1 | $759.00 | $759.00 | 
| USB Ethernet Adapter | USB NIC | Identification System | CableCreation | 1 | $15.99 | $15.99 |
| Siemens Memory Card | SIMATIC memory card | Identification System | Allied Electronics / 6ES7-954-8LC03-0AA0 | 1 | $90.96 | $90.96 |  
|  |  |  | **Components** | 8 | **Total Cost** | $1006.90 |  