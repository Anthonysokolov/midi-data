import mido
from random import randint

def ascending(num=7, start=0, step=1):
    return [mido.Message("note_on", note = start + i*step)for i in range(num)]

def descending(num=7, start=127, step=1):
    return [mido.Message("note_on", note = start - i*step)for i in range(num)]

def randAsc(num=7, start=0, vel=8):
    out = []
    current = start
    for i in range(num):
        out.append(mido.Message("note_on", note = current))
        current = current + randint(0,vel)

    return out

def randDesc(num=7, start=127):
    out = []
    current = start
    for i in range(num):
        out.append(mido.Message("note_on", note = current))
        current = current - randint(1,9)

    return out

def randWalk(num=7, start=64, lower=0, upper=127, vel=7):
    out = []
    current = start
    for i in range(num):
        out.append(mido.Message("note_on", note = current))
        current = current + randint(-vel,vel)
        if current < lower:
            current = lower + randint(0,vel)
        if current > upper:
            current = upper - randint(0,vel)

    return out
