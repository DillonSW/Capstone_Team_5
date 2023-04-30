# OPC Test Code

### Function
The OPC test file allowed the team to edit and try different commands when communicating with the PLC. 
Commands like read and write were needed for the main program to function properly.
The highlighted code was used with Controller tags to correctly send and receive data. 
The commented out portion was a first attempt to write to PLC input and output tags.

### Dependancy 
To correctly use the OPC code with an Allen Bradley PLC, pycomm3 must be included installed on the host machine.  
You will also need to import LogixDriver to connect directly through the PLC IP address. 

### Installation
You will first need to install python3 to the host machine before python can be used. Use the command below in a linux terminal.  
Command : sudo apt install python3  
If the command : pip3 --version returns a result, continue. Otherwise use : sudo apt install python3-pip.  

Then install pycomm3 using the command : pip install pycomm3. It may be reasonable to use sudo to overcome any path dependency errors

### Running
To run the program, you will need to create a static IP on the host machine to be on the same network.  
When using the PLC Lab, the static IP was used as 192.168.100.98 with a subnet mask of 255.255.255.0.  
The DNS can be left to automatically assign itself. Make sure the PLC IP is given in the code to the logixDriver.  

After all of that is done and tested using ping, you can run the program from the terminal.  
