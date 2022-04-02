from src.OpenCV import OpenCV
from pynput import keyboard

overwatch = Overwatch()

def on_release(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    print('Key released: ' + k)


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['f1']:
        overwatch.ps
        # return False

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # start to listen on a separate thread
listener.join()   # remove if main thread is polling self.keys

# def on_press(key):
#     pressed.add(key)
#     print(pressed)
#     for c in COMBINATIONS:
#         for keys in c["keys"]:
#             if keys.issubset(pressed):
#                 if (c["command"] == "Headshot"):
#                     overwatch.ss()
#                     print("Hi")
#                 if (c["command"] == "Exit"):
#                     exit()

# def on_release(key):
#     if key in pressed:
#         pressed.remove(key)
