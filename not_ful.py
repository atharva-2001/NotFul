import psutil
from sys import exit

from subprocess import Popen
from os import getcwd
from warnings import filterwarnings
filterwarnings("ignore")

import os
from win32com.client import Dispatch

# this code adds the exe file in the startup registry

try:
    path = r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(os.getlogin())

    path = os.path.join(path, "not_ful.lnk")
    path2 = os.getcwd()
    path2 = path2.encode('unicode-escape').decode('ascii')
    target =path2 + r"\not_ful.exe"
    wDir = path2
    icon = path2 + r"\not_ful.exe"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

except:
    pass


# import package to wait
from time import sleep

# checks if the data is in value.txt 
# and accordingly either asks data
# or does the normal notification job

log = open('value.txt',"r+")
values = log.readlines()
log.close()
if values == []:  # file is empty
    log.close()
    log = open('value.txt','w+')
    print("no value found in value.txt")
    # ask for input
    print("""
        Enter the value you want to be notified at.
        You will be notified between every 100 secs(default),
        when the battery has reached that value.
    """)
    preset = int(input("Enter the value here: "))
    duration = int(input("Enter the duration between which you want to be notified at: "))
    # save the preset value in log file
    log.write('the value of battery is: ')
    log.write(str(preset))
    log.write('\n')
    log.write('the value of the duration is:  ')
    log.write(str(duration))
    log.close()

else:
    os.system('python test.pyw')







