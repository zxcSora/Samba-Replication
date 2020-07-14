#!/usr/bin/python3
import os
import sys
import subprocess

shell_command = subprocess.run(['samba-tool', 'drs', 'showrepl'], stdout=subprocess.PIPE)
decode = shell_command.stdout.decode('utf-8')
dirty_list = decode.split("\n\n")
context_for_check = sys.argv[1]
direction_for_check = sys.argv[2]
almost_clear_list = []

for i in range(0, len(dirty_list)):
    a = dirty_list[i]
    if a.find("DC=local") > -1:
        almost_clear_list.append(a)
del almost_clear_list[-1]

if direction_for_check == "in":
    for i in range(0, 6):
        del almost_clear_list[0]
elif direction_for_check == "out":
    for i in range(0, 6):
        del almost_clear_list[-1]
else:
    print("Specify valid ARG2")
    sys.exit(255)

for i in range(0, len(almost_clear_list)):
    if almost_clear_list[i].find(context_for_check) > -1:
        if almost_clear_list[i].find("was successful") > -1:
            if context_for_check == "CN=Configuration,DC=bbgroup,DC=local":
                    if almost_clear_list[4].find("was successful") > -1:
                        print(context_for_check + " successful") # or print("0") for zabbix
                        sys.exit()
                    else:
                        print(context_for_check + " fail") # or print("1") for zabbix
                        sys.exit()

            elif context_for_check == "DC=bbgroup,DC=local":
                if almost_clear_list[2].find(context_for_check) > -1:
                    if almost_clear_list[2].find("was successful") > -1:
                        print(context_for_check + " successful") # or print("0") for zabbix
                        sys.exit()
                    else:
                        print(context_for_check + " fail") # or print("1") for zabbix
                        sys.exit()

            print(context_for_check + " successful") # or print("0") for zabbix
        else:
            print(context_for_check + " fail") # or print("1") for zabbix