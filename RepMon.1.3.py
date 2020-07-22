#!/usr/bin/python3
import os
import sys
import subprocess

def replication_check(context):
    context_for_check = context.replace('.', ',')
    command = ['samba-tool', 'drs', 'replicate', 'pdc1', 'pdc2', context_for_check]
    shell_command = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    decode = shell_command.stdout.decode('utf-8')
   #print(decode)
    if decode.find("was successful") > -1:
        return 0
    else:
        return 1

print(replication_check(sys.argv[1]))
