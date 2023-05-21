window_title = "Roblox" # Change to any window name to lock it on it

import pygetwindow as gw
window = gw.getWindowsWithTitle(window_title)[0]

if window.title == window_title: # GetWindow re turns any window containing a title so you have to check
    print("Ready to go!") # Window exits with the correct name
else:
    from sys import exit
    input(f'A window called "{window_title}" isn\'t open!\nPress enter to close')
    exit()

# I don`t see a reason to import unless everything is ready
from win32gui import GetWindowText, GetForegroundWindow
from win32.win32api import GetKeyState
from time import sleep
import pyautogui

first_toggle = False

def first_check(first_toggle): # This is not the best way to do it but i don't care rn
    if (GetKeyState(0xDC) < 0):
        while (GetKeyState(0xDC) < 0):
            pass
        return not first_toggle
    else:
        return first_toggle

print("\nPress \\ To toggle First person\nStatus:")

while True:
    window_center_x = window.left + (window.width // 2)
    window_center_y = window.top + (window.height // 2)
    curr_window_title = GetWindowText(GetForegroundWindow())

    mouse_x, mouse_y = pyautogui.position()

    print(f'First Person lock: {first_toggle}          ',end='\r')
    while (GetKeyState(0x02) < 0) or first_toggle:
        if (curr_window_title == window_title):
            if first_toggle:
                pyautogui.moveTo(window_center_x, window_center_y, duration=0)
            else:
                pyautogui.moveTo(mouse_x, mouse_y, duration=0)
        first_toggle = first_check(first_toggle)
    
    first_toggle = first_check(first_toggle)

    sleep(0.01)
