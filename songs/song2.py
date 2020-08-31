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



for loop in range(3):
    # generate messages
    #msg = mido.Message("note_on",note=57 + 2*loop)
    size = 6
    messages = p.randAsc(size,start=57+loop,vel=3)

    for y in range(7,11):
        i = 0.01
        j = 0.001

        for x in range(y):
            msg = messages[x % size]
            outport.send(msg)
            time.sleep(i+j)

            temp = i
            i = i+j
            j = temp

        time.sleep(1/y)
    time.sleep(.35)
