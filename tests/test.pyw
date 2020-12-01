
import psutil
from sys import exit

from subprocess import Popen
from os import getcwd
from warnings import filterwarnings
filterwarnings("ignore")

import os
from win32com.client import Dispatch
from time import sleep
log = open('value.txt',"r+")
values = log.readlines()
log.close()

# print("the battery is {} plugged".format("" if charge_status is True else "Not"))

# import package to wait
from time import sleep

# import package to show notifaction
from win10toast import ToastNotifier
os.system('cls')

try:
    print(values)
    preset = int(''.join(filter(str.isdigit, values[0])))       
    duration = int(''.join(filter(str.isdigit, values[1])))
    # print(preset)
except Exception as e:
    print(e)
    sleep(10)
    exit(0)


while(1):
    # get battery related information
    battery = psutil.sensors_battery()

    # battery percent
    percent = int(battery.percent)

    # to check whether plugged or unpluugged
    charge_status = battery.power_plugged
    percent = int(battery.percent)

    # if this is bigger than a pre-set value, we put a message.
    # the user will then maybe stop charging and the battery charge will fall
    flag = battery.power_plugged
    if flag is True:
        if percent >= preset:
            try:
                # toast windows message for win10 
                toaster = ToastNotifier()
                toaster.show_toast("Bat_Not Notifier","Battery percent above {}".format(preset),duration=10)
            except:
                # otherwise, run the bat file
                p = Popen("notifier.bat", cwd = getcwd(),shell =False )
                stdout, stderr = p.communicate()
    os.system('cls')
    print('The battery is at {}%'.format(percent))
    print('The battery is {check}plugged'.format(check="" if flag is True else "un"))
    print('The value you set is {} and the duration is {}'.format(preset,duration))
    # else the program runs as it is, checking the percentage every 30 seconds
    sleep(duration)



