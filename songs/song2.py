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

# generate messages
msg = mido.Message("note_on",note=57)


for note in range(57,71,2):
    msg = mido.Message("note_on",note=57)
    i = 0.001
    j = 0.001

    for x in range(13):
        outport.send(msg)
        time.sleep(i+j)

        temp = i
        i = i+j
        j = temp

    time.sleep(.3)
