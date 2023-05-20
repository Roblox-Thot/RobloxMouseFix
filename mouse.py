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
import pyautogui

while True:
    window_x, window_y, window_width, window_height = window.left, window.top, window.width, window.height
    curr_window_title = GetWindowText(GetForegroundWindow())

    mouse_x, mouse_y = pyautogui.position()

    while (GetKeyState(0x02) < 0):
        if (curr_window_title == window_title):
            pyautogui.moveTo(mouse_x, mouse_y, duration=0)
