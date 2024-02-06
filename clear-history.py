# All The Imports 

from pynput.mouse import Controller as ControllerM, Button
import time
import webbrowser

# Opening Web Browser

def webbrows():

    url = 'https://www.google.com/'
    webbrowser.open(url)

# Clear History Function

def clear_history():

    mouse = ControllerM()
    time.sleep(0.5)
    mouse.position = (1896, 62)
    mouse.click(Button.left)
    time.sleep(0.5)
    mouse.position = (1697, 289)
    time.sleep(0.5)
    mouse.position = (1450, 281)
    time.sleep(0.5)
    mouse.click(Button.left)
    time.sleep(0.5)
    mouse.position = (133, 259)
    time.sleep(0.5)
    mouse.click(Button.left)
    time.sleep(0.5)
    mouse.position = (1146, 694)
    time.sleep(0.5)
    mouse.click(Button.left)
    time.sleep(2)
    mouse.position = (1897, 24)
    mouse.click(Button.left)

#Run
webbrows()
time.sleep(2)
clear_history()
