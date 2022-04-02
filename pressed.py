from src.Overwatch import Overwatch
from pynput import keyboard
import subprocess

overwatch = Overwatch()

pressed = set()

COMBINATIONS = [
    {
        "keys": [{keyboard.KeyCode(char="a")}],
        "command": "Headshot",
    },
    {
        "keys": [
            {keyboard.Key.cmd, keyboard.KeyCode(char="c")},
            {keyboard.Key.cmd, keyboard.KeyCode(char="C")},
        ],
        "command": "Exit",
    },
]

def on_press(key):
    pressed.add(key)
    print(pressed)
    for c in COMBINATIONS:
        for keys in c["keys"]:
            if keys.issubset(pressed):
                if (c["command"] == "Headshot"):
                    overwatch.ss()
                    print("Hi")
                if (c["command"] == "Exit"):
                    exit()

def on_release(key):
    if key in pressed:
        pressed.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
