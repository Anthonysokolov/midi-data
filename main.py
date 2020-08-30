'''
Program to send midi data from python to a midi port
Made to use with hardware synths!
'''

import mido
import time

import patterns

# Connect port, change port name as needed
port = "minilogue SOUND"
outport = mido.open_output(port)

for i in range(5):
    # generate messages
    messages = patterns.descending(10,80,4)

    # send messages to output
    for msg in messages:
        outport.send(msg)
        time.sleep(.2)
