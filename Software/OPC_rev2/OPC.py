import pycomm3

from pycomm3 import LogixDriver

with LogixDriver('192.168.100.210') as plc:

    #tag_value = plc.read('Local:1:O.Data.2')
    #print(f'The value of OPC_Test is {tag_value}')
    
    #tag_value = plc.write('Local:1:O.Data.2',True)
    #print(f'The value of OPC_Test is {tag_value}')
    
    tag_value = plc.read('OPC')
    print(f'The value of OPC_Test is {tag_value}')
    
    tag_value = plc.write('OPC',True)
    print(f'The value of OPC_Test is {tag_value}')
    
    tag_value = plc.read('Slot.ACC').value
    print(f'The value of Slot is {tag_value}')
    
    tag_value = plc.read('Level.ACC').value
    print(f'Value of Level: {tag_value}')
    
    
    
    

