# PLC Code

### Function

This software file is the PLC .ACD file for controlling the motor and interacting with the OPC client.

**PLEASE NOTE:** This .ACD file is usable for the Allen Bradley PLCs in the ATC lab in Prescott Hall. If future work is to be done with the gifted Siemens PLC, the .ACD code must be copied over to a ladder logic file in TIA Portal.

The PLC code uses 2 TON timers to control when the motor receives pulses (sort of like PWM). There is a way to be able to do this with 1 TON timer, but I don't remember how. Essentially you must make PLC code for rising-edge detection.

The PLC has 2 tags that are written to by the OPC (Look in the Controller Tags section. Also see the code for the OPC to see the written values). These tags controll whether or not the system is distributing boards, or is having boards loaded.

### Installation

More likely than not, you will be running this code in the PLC labs of Prescott. Download the .ACD file and email it to your Tech email. If you are on a school computer, you could also save it to your lab drive. When in the PLC labs, either download the file from your email or your lab drive. Open Studio 5000 and select Existing Project. From there you should be able to edit the code.

### Running

To run the code, you must select your computer from the dropdown Communication -> Who Active. To do so, you must select Set Project Path. Afterwards, for testing, you must select Communication -> Download. This will save your changes and download them to the PLC. If it does not automatically put you in Run Mode or Online, you must select it again from the Communication dropdown.
