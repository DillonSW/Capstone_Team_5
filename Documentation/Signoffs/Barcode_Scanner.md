# Barcode Scanner Subsystem  

## Subsystem Function  

This Subsystem's role in the team's design is to scan barcodes on school devices before being placed into the machine. This is done to number a device in each slot so a student can be assigned the number when renting the device, and is also  done to assure that devices are accounted for.  

## Constraints  

* Shall be low power and consume no greater than 5 V 0.5 A. This is due to being powered by the miniPC. Common computers only output a max rating of 5 V 0.5 A.  
^ Source: https://resources.pcb.cadence.com/blog/2020-what-are-the-maximum-power-output-and-data-transfer-rates-for-the-usb-standards  

* Shall be powered by a USB port to connect with the miniPC  

* Barcodes shall be of decent quality to follow ISO 15416 standard. Assures that the codes can be read by any scanner  

## Schematic  


## Analysis  

To verify correct operation of the scanner, a USB voltmeter will be used connecting the scanner to the PC. This will allow the team to monitor the scanner during operation and ensure the 5 V 0.5 A limit is not exceeded. The Scanner shall be a 2D barcode scanner that is able to decode both 1D and 2D codes. The code the team is using is a 1D Code 128 barcode that can be read by the module. They are easy to design and will be cheap to order for the devices.  

The current USB voltmeter in mind is the 2 in 1 USB micro and type C connector and the scanner is the Waveshare USB scanner module that will work along the PC.  
The voltmeter is able to monitor the Voltage and Current taken by the Module. A benefit of the meter is the ability to verify operating current and voltage when a box is scanned.  

The scanner will be used at different ranges to determine an appropriate range for a box to be placed and still be correctly read. To verify the code information, the scanner output will be compared with the expected outcome to ensure a box is not mislabeled.  

## BOM  

| Name of item | Description | Subsystem | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|--------------|----------|-------|-------|
| Eversame 2 in 1 USB Tester | Voltmeter | Barcode Scanner | Eversame | 1 | $22.99 | $22.99 |  
| Barcode Scanner Module | 1D/2D Code Reader | Barcode Scanner | Waveshare | 1 | $39.99 | $39.99 |  
|  |  |  | **Components** | 2 | **Total Cost** | $62.98 |  
