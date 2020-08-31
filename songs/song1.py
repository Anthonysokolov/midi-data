'''
Program to send midi data from python to a midi port
Made to use with hardware synths!
'''

import mido
import time
import sys

sys.path.append("..")

import patterns

# Connect port, change port name as needed
port = "minilogue SOUND"
outport = mido.open_output(port)

while True:
    # generate messages
    #messages = patterns.descending(5+i,127 - 4*i,4)
    #messages += patterns.ascending(3, 99-4*i, 4)
    messages = patterns.descending(start = 90, step=4)
    messages = patterns.randWalk(12,start = 72, vel=5)

    # send messages to output
    for msg in messages:
        outport.send(msg)
        time.sleep(.2)
