'''
Program to send midi data from python to a midi port
Made to use with hardware synths!
'''

import mido
import time

# Connect port, change port name as needed
port = "minilogue SOUND"
outport = mido.open_output(port)

# generate messages
messages = [mido.Message("note_on", note = 20 + i*2 )for i in range(30)]

# send messages to output
for msg in messages:
    outport.send(msg)
    time.sleep(.25)
