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

for j in range(3):
    for i in range(7):
        # generate messages
        #messages = patterns.descending(5+i,80 - 4*i,4)
        #messages += patterns.ascending(3, 40-4*i, 4)
        messages = patterns.randAsc(10,20)

        # send messages to output
        for msg in messages:
            outport.send(msg)
            time.sleep(.15)
