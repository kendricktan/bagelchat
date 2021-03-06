import os
import socket
import struct
import sys
import thread

from send import *
from recv import *
from gui import *
from cli import *

# Checks for usage help
if len(sys.argv) > 1:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':   
        print 'Usage: python setup.py [username] [multicast address] [multicast port]'
        print '#### All fields are optional ####'
        sys.exit()

# Clears screen
os.system('cls')

# Multicast settings
MULTICAST_USERNAME = str(sys.argv[1]) if len(sys.argv) > 1 else 'Anonymous'
MULTICAST_ADDY = str(sys.argv[2]) if len(sys.argv) > 2 else '224.3.29.71'
MULTICAST_PORT = int(sys.argv[3]) if len(sys.argv) > 3 else 32767

'''
bc_cli = bagelchat_cli(MULTICAST_USERNAME, MULTICAST_ADDY, MULTICAST_PORT)
loop_cli(bc_cli)
'''

bc_gui = bagelchat_gui(None, MULTICAST_USERNAME, MULTICAST_ADDY, MULTICAST_PORT)
loop_gui(bc_gui)
