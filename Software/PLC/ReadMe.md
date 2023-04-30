This software file is the PLC .ACD file for controlling the motor and interacting with the OPC client.

**PLEASE NOTE:** This .ACD file is usable for the Allen Bradley PLCs in the ATC lab in Prescott Hall. If future work is to be done with the gifted Siemens PLC, the .ACD code must be copied over to a ladder logic file in TIA Portal.

The PLC code uses 2 TON timers to control when the motor receives pulses (sort of like PWM). There is a way to be able to do this with 1 TON timer, but I don't remember how. Essentially you must make PLC code for rising-edge detection.

The PLC has 2 tags that are written to by the OPC (Look in the Controller Tags section. Also see the code for the OPC to see the written values). These tags controll whether or not the system is distributing boards, or is having boards loaded.
