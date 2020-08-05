#!/usr/bin/python3

import socket
import sys
import os
import time

#if len(sys.argv)<2:
#    sys.stderr.write('need a port number\n')

#sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sock.bind(('0.0.0.0',int(sys.argv[1])))

while True:
    time.sleep(300)
    try:
        os.system('git pull')
        os.system('bash runme.sh')
    except:
        pass
