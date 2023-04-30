# Klaw Rev. 3
Klaw came about as a joke the team made during the first semester of capstone.  
We joked we would just make a claw machine where students needed to fish out the device they need for a lab.  

### Function
Klaw3.py is the main functional program of the capstone.  
It contains the code needed to create the GUI, access the database, and message the PLC.

### Dependancy 
* mysql.connector - installed from the same site as the workbench.  
* PySimpleGUI - installed through the command line. Use sudo pip. 
* datetime    - installed through the command line.  
* pycomm3     - installed through the command line.   

### Installation
Install mysql.connector either from the terminal or from the webiste. Make sure it is the connector for python.  
To install all python libraries listed, use: Sudo pip install <library>.  
You can always use: <library> --version to check installations.  
  
### Running
The file can be run through the terminal. You will need to have the OPC operational to actually run the program though.  
The directions for OPC are in the OPC software folder.  
