# Author: Phillip Edwards
# Project: Auto Clicker
# Class: clicker.py
# Citation for program: https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/
# Date: May 13, 2021

import time
import threading

# pynput module imports
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Control The Click Variables

delay = 0.01 # Delay in seconds
button = Button.left  # Button for the auto clicker to use.
start_stop_key = KeyCode(char='a') # Start and stop key for the clicker clicks
stop_key = KeyCode(char='b') # Kill the thread key for the clicker

# Class for controlling the clicks -> Ran on a separate thread
class ClickMouse(threading.Thread) :
    # Constuctor for mouse
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    # Starts the clicking
    def start_clicking(self):
        self.running = True

    # Stops the clicking
    def stop_clicking(self):
        self.running = False

    # Exits the thread
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # Runs the thread
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

# Sets up the Mouse
mouse = Controller()

# Sets up the thread
click_thread = ClickMouse(delay, button)

# Starts the thread
click_thread.start()

# Determines what happens on a key press
def on_press(key):
  # start_stop_key will stop clicking 
  # if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
              
    # here exit method is called and when 
    # key is pressed it terminates auto clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()
  
  
# Event listener for the key press
with Listener(on_press=on_press) as listener:
    listener.join()
