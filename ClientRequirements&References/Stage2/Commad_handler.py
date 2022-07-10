#***********************************************************************
#*
#* POS software with Scan Direction detection using openCV 
#*
#***********************************************************************
#Version history
#01 
# Code version before integrating UI. Motion is tested on command line.
#02
#Added GUI. Running motion detection as a thread. Has sync issues with 
#bar code data. Testing in prgress.. Direction detection, bar code 
# aquisition and GUI window is working. Working on UI data update.

import threading   
from collections import Counter as count
import datetime
from collections import deque
import os
import time
from time import sleep, perf_counter
import sqlite23

def OnHelp():
    print('help - List available commands')
    print('exit - Kill this program')
    print('update - Make a new entry into the Database')
    print('dump - dump the contents of the DB')
def CommandHandler(command):
    global terminateThreads
    if command == 'help':
        print("CommandHandler help")
        OnHelp()
    elif command == 'ip':
        print("CommandHandler ip address")
    elif command == 'exit':
        print("CommandHandler exit")
        terminateThreads = 0
        exit()
    elif command == 'update':
        sqlite23.UpdateElement()
    elif command == 'dump':
        sqlite23.readSqliteTable()
        

terminateThreads = 1
def RegistrationFunction():
    global leftMotionPoints 
    global RightMotionPoints
    global idleStatePoints
    global firstCenterAq
    global lastCentrePoint
    global direction
    global last_direction
    global objectMovement
    global objectMovementReadPending
    global terminateThreads
    while(terminateThreads):
        barcodeDataReady = 1
        sleep(1)
        #print('RegistrationFunction')

def CommandReaderFunction():
    #input = 'sdsdd'
    global barcodeDataReady
    global terminateThreads    
    while(terminateThreads):
        #print('CommandReaderFunction')
        command = input()
        CommandHandler(command)
        #input=input()
        #print(command)
        #sleep(1)
        barcodeDataReady = 1
 
def GuiUpdate():
    global objectMovement
    global objectMovementReadPending
    global barcodeDataReady

class Item:
    def __init__(self, name, price, button):
        self.name = name
        self.price = price
        self.button = button
        

class Register:
    def __init__(self, parent):
        self.parent = parent
        parent.title('ZEBRA Point of Sale Software')

    

CommandReaderThread    = threading.Thread(target=CommandReaderFunction)
RegistrationThread = threading.Thread(target=RegistrationFunction)
#GuiUpdateThread      = threading.Thread(target=GuiUpdate)

sqlite23.InitDatabse()
print('\n\n**************  MASTER STATION  **************\n\n')

print('Enter commands, help to list available commands')
CommandReaderThread.start()
RegistrationThread.start()
#GuiUpdateThread.start()
CommandReaderThread.join()
RegistrationThread.join()
#root.mainloop()



