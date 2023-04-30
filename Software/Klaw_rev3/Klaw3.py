# Author : Dillon Williams & Nidhay Patel
# Date : 4/3/2023
# Name : Klaw3.py
# Description : This program creates the GUI, performs operations on the machine database, and signals the PLC

import mysql.connector
from mysql.connector import Error	# required to run sql queries
import PySimpleGUI as sg		# needed to make the GUI
from datetime import datetime		# Tracks load/store of devices
import pycomm3
from pycomm3 import LogixDriver		# Needed to communicate with the PLC

with LogixDriver('192.168.100.210') as plc:  # The IP of the PLC used (change when next team uses donated PLC)

    #Screen theme
    sg.theme('Black')

    #Sizing of text on the UI
    font1=('Times New Roman', 30)
    font2=('Times New Roman', 14)
    font3=('Times New Roman', 12)
    
    # List1 - List of classes on GUI
    # List2 - List of class terms

    list1 = ['ECE 2140 - Digital Systems','ECE 3130 - Microprocessor Systems','ECE 3710 - Intro to Telecomm','ECE 3140 - Digital Systems Design','ECE 4140 - Embedded Systems']
    list2 = ['Freshman','Sophomore','Junior','Senior']

    #Creates the GUI layout on the screen for the machine
    # VPush - centers vertically
    # Push  - centers horizontally
    # Text  - makes text on the screen
    # Combo - drop down list
    # Checkbox - initializes blank
    
    frame_1 = [
        [sg.VPush()],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text('ECE Equipment Checkout Form',font=font1), sg.Push(),],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text('TechID',font=font2),sg.Input(size =(30, 1), do_not_clear=False, font=font3), sg.Push(),],
        [sg.Push(), sg.Text(''), sg.Push(),],
        [sg.Push(), sg.Text(' Name ',font=font2),sg.Input(size =(30, 1), do_not_clear=False, font=font3), sg.Push(),],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text(' Email ',font=font2),sg.Input(size =(30, 1), do_not_clear=False, font=font3), sg.Push(),],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text('Course',font=font2),sg.Combo(list1, default_value='ECE 2140 - Digital Systems', font=font3, size=(28,1), readonly=True), sg.Push(),],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text(' Term ',font=font2),sg.Combo(list2, default_value='Freshman', font=font3, size=(28,1), readonly=True), sg.Push(),],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text('')],
        [sg.Push(), sg.Text('I understand that failure to return this equipment at end of the semester may \nresult in: \n\n       1. Charging my Student Account \n       2. Holding my grades \n       3. Disciplinary Action', font=font2), sg.Push(),],
        [sg.Push(), sg.Checkbox('', default=False, key="-IN-", font=font2), sg.Text('I agree', font=font2), sg.Push()],
        [sg.Push(), sg.Submit(), sg.Push(),],
        [sg.Push(), sg.Text('')],
        [sg.VPush()]
    ]

    # Layout of the main window, colors are assigned to push statements to avoid blocks on the screen
    # Frame is the black box in the screen
    layout = [
        [sg.VPush(background_color='#7851a9')],
        [sg.Push(background_color='#7851a9'), sg.Frame('', frame_1, size=(680,730), border_width=(10), title_location=sg.TITLE_LOCATION_TOP), sg.Push(background_color='#7851a9')],
        [sg.VPush(background_color='#7851a9')]
    ]

    #Makes window 1920x1080 and links to the top of the screen so it cannot be closed without a combination
    window = sg.Window("Klaw", layout, no_titlebar=False, location=(0,0), size=(1920,1080), background_color='#7851a9', finalize=True)

    # Button to close the program
    window.bind('<Alt-z>', 'Minimize')

    #Keeps track of loaded boards to verify input
    boardCount = 0
    numberRented = 0

    while True:

        #Takes values from screen text boxes
        event, values = window.read()

        if event== 'Minimize': # Receive point of bind button
            window.close()
            break
        else:
            ID = values[0] 	#Stored values 
            Name = values[1]
            Email = values[2]
            course = values [3]
            term = values[4]
            check = values["-IN-"]

            CorrectEmail = Email.endswith("@tntech.edu")

        if ID in ['delete', 'Delete'] and Name in ['admin', 'Admin']:   #Connects to and deletes all data from the database given the correct input
            print("Deleting Data")
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='capstone5',
                                                     user='root',
                                                     password='S112Y568b@')

                cursor = connection.cursor(prepared=False) # prepared = False means no input from the user is used in the query

                sql_insert_query1 = """delete from students;"""
                sql_insert_query2 = """delete from inventory;"""

                cursor.execute(sql_insert_query1)
                cursor.execute(sql_insert_query2)
                connection.commit()
                print("Data Deleted from Database")
                sg.popup("Data Deleted from Database", title="Admin", keep_on_top=True) # Signals data is deleted

            except Error as error:
                print("Query Failed {}",error)   # Catches Query errors
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection was closed")

        elif ID in ['load', 'Load'] and Name in ['admin', 'Admin']: # Allows the admin to load devices into the machine
            print("Loading Inventory")
            layout2 = [
                [sg.Text('Box Number',font=font2),sg.Input(size =(30, 1), do_not_clear=False, font=font3)],   # Popup where boxes are entered
                [sg.Submit()]
            ]

            window2 = sg.Window('Load Mode', layout2, keep_on_top=True, modal=True)  # modal - remains open after an entry
            LoadedBoards = []
            while True:

                event, values = window2.read()
                
                plc.write('LoadBegin',True)    # Signal to PLC that the user is loading devices

                if event == sg.WIN_CLOSED:  #When complete, show the devices that were loaded
                    print(boardCount)
                    print(LoadedBoards)
                    print(StepCount)
                    print(levelCount)
                    plc.write('LoadDone', True)   # Signal the user is finished loading to reset the PLC location
                    plc.write('Empty', True)      # Clear values
                    plc.write('Empty', False)
                    string = ', '.join([str(i) for i in LoadedBoards])
                    sg.popup("Loading Complete", f"The following Boards have been stored: \n", f"{string}")
                    break
                else:
                    try:
                        StepCount = str(plc.read('Slot.ACC').value)   # Takes location of board from PLC
                        RentStep = str(plc.read('Slot.ACC').value)
                        levelCount = str(plc.read('Level.ACC').value)
                        RentLevel = str(plc.read('Level.ACC').value)
                        
                        connection = mysql.connector.connect(host='localhost',
                                                            database='capstone5',   #The %s is used to help prevent SQL Injection
                                                            user='root',
                                                            password='S112Y568b@')

                        cursor = connection.cursor(prepared=False)

                        Box = values[0]
                        Time = datetime.now().strftime("%Y/%m/%d %H:%M:%S") # Returns the current time (not exact)

                        sql_insert_query1 = """insert into inventory(boxNumber, date_stored) values(%s,%s);"""
                        sql_insert_query2 = """update inventory set step = %s, deviceLevel = %s where boxNumber = %s;"""
                        value1 = (Box,Time)
                        value2 = (StepCount, levelCount, Box)

                        cursor.execute(sql_insert_query1, value1)
                        cursor.execute(sql_insert_query2, value2)
                        connection.commit()
                        print("Data Added to Inventory")
                        boardCount = boardCount + 1
                        LoadedBoards.append(Box)
                        plc.write('OPC', True)  # Tell the PLC to move to the next slot

                    except Error as error:
                        print("Query Failed {}",error)
                        sg.popup("That board is already stored!", keep_on_top=True, title="Error") # Tell the user if a repeat occurs
                    finally:
                        if connection.is_connected():
                            cursor.close()
                            connection.close()
                            print("MySQL connection was closed")

        elif (len(Name.split()) > 2) or (len(Name.split()) == 1):
            sg.popup("Name field is not correct. Enter your first and last name.", keep_on_top=True, title="Error")  # Next several lines are error-checking input boxes

        elif not ID or not Name or not Email:
            sg.popup("All Fields must be filled", keep_on_top=True, title="Error")

        elif not values[0][0] =='T':
            sg.popup("The ID must include the T", keep_on_top=True, title="Error")

        elif not CorrectEmail:
            sg.popup("Email must end in @tntech.edu", keep_on_top=True, title="Error")

        elif check:
            try:

                StepCount = str(plc.read('Slot.ACC').value)
                RentStep = str(plc.read('Slot.ACC').value)
                levelCount = str(plc.read('Level.ACC').value)
                RentLevel = str(plc.read('Level.ACC').value)

                connection = mysql.connector.connect(host='localhost',
                                                    database='capstone5',
                                                    user='root',
                                                    password='S112Y568b@')

                cursor = connection.cursor(prepared=True)

                sql_insert_query1 = """select boxNumber from inventory where date_rented is null and step = %s and deviceLevel = %s;"""
                value1 = (RentStep, RentLevel)
                cursor.execute(sql_insert_query1, value1)
                Board = cursor.fetchone()
                if Board is not None:              # Returns the next board that has not been rented by location in the machine
                    try:
                        Board = str(Board[0])
                        Time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                        sql_insert_query2 = """insert into students(id) values(%s);"""
                        sql_insert_query3 = """update students set email = %s, student_name = %s, course = %s, term = %s where id = %s;"""
                        sql_insert_query4 = """update students set boxNumber = %s where id = %s;"""
                        sql_insert_query5 = """update inventory set date_rented = %s where boxNumber = %s;"""

                        value2 = (ID,)
                        value3 = (Email,Name,course,term,ID)
                        value4 = (Board,ID)
                        value5 = (Time,Board)

                        cursor.execute(sql_insert_query2, value2)
                        cursor.execute(sql_insert_query3, value3)
                        cursor.execute(sql_insert_query4, value4)
                        cursor.execute(sql_insert_query5, value5)
                        connection.commit()

                    except Error as error:
                        print("Query Failed {}",error)
                        sg.popup("That Board is already Rented!", keep_on_top=True, title="Error")

                    finally:
                        if connection.is_connected():              # If the board existed, rent and apply to the user. Then notify the received board number.
                            cursor.close()
                            connection.close()
                            tag_value = plc.write('OPC',True)
                            sg.popup("Board Registration Complete!", f"The following Board has been Rented: ", f"{Board}", title="Complete")
                else:
                    sg.popup("There are no available Devices!", keep_on_top=True, title="Error")

            except Error as error:
                print("Query Failed {}",error)
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else:
            sg.popup('You must agree to the terms!', title="Error") 
