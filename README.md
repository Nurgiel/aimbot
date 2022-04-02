### OpenCV Aimbot
-Install VS Code and Python
  - [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
  - [https://www.python.org/downloads/](https://www.python.org/downloads/)
    - Add Python to Environmental Variables
  - Remove Python installer from Start -> Manage app execution aliases
- Install pip and required packages
  - `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
  - `py .\get-pip.py`
  - `pip install --upgrade pip`
  - `pip install opencv-contrib-python`
  - `pip install pyautogui`
  - `pip install Pillow --upgrade`
  - `pip install ahk`
  - `pip install keyboard`
  - `pip install pynput`
- Run Application
  - `export QT_DEBUG_PLUGINS=1` (Debug)
  - `python read.py`

https://stackoverflow.com/questions/59191177/listen-for-a-shortcut-like-wina-even-if-the-python-script-does-not-have-the-f (focus)