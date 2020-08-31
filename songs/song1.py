'''
Program to send midi data from python to a midi port
Made to use with hardware synths!
'''

import mido
import time
import sys
from random import randint

sys.path.append("..")

import patterns as p

# Connect port, change port name as needed
port = "minilogue SOUND"
outport = mido.open_output(port)

while True:
    # generate messages
    messages = p.ascending(5, start=67,step=3)
    messages.append(None)
    messages += p.ascending(5, start = 64, step=3)
    messages.append(None)
    messages += p.randWalk(7, start=71, vel=3)

    # send messages to output
    for msg in messages:
        if msg:
            outport.send(msg)
            amt = 0.05 * randint(4,8)
            time.sleep(amt)
        else:
            time.sleep(0.3)

    time.sleep(0.5)
