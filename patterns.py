import mido

def ascending(num=7, start=0, step=1):
    return [mido.Message("note_on", note = start + i*step)for i in range(num)]

def descending(num=7, start=100, step=1):
    return [mido.Message("note_on", note = start - i*step)for i in range(num)]
