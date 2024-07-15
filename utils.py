import pydirectinput as keys 
from threading import Event
channel_id = ["1262326547658969119", "1208458193408368680"]
drive_mode = False

def check_channel(id):
    return id in channel_id

def hold_key(key, time, duty_cycle=1):
    alternate = True
    while time > 1:
        if alternate:
            keys.keyDown(key)
            Event().wait(duty_cycle)
            alternate = False
        else:
            keys.keyUp(key)
            Event().wait(1 -duty_cycle)
            alternate = True

        time-=1

    if time > 0 and alternate:
            keys.keyDown(key)
            Event().wait(time)
            keys.keyUp(key)

