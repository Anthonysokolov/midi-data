import mido
from random import randint

def ascending(num=7, start=0, step=1):
    return [mido.Message("note_on", note = start + i*step)for i in range(num)]

def descending(num=7, start=100, step=1):
    return [mido.Message("note_on", note = start - i*step)for i in range(num)]

def randAsc(num=7, start=12):
    out = []
    current = start
    for i in range(num):
        out.append(mido.Message("note_on", note = current))
        current = current + randint(1,9)

    return out
