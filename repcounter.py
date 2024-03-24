import keyboard # pip install keyboard
import sys
import time
import platform
import csv
from datetime import date

if platform.system() == 'Windows':
    import win32gui # pip install pywin32
elif platform.system() == 'Darwin':
    from AppKit import NSWorkspace

start_time = time.time()
counter = 0
elapsed_time = 0
unfocused_time = 0

def is_terminal_in_focus():
    if platform.system() == 'Windows':
        current_window = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(current_window)
        return "Command Prompt" in window_title or "Windows PowerShell" in window_title or "Terminal" in window_title
    elif platform.system() == 'Darwin':
        active_app = NSWorkspace.sharedWorkspace().activeApplication()
        return active_app['NSApplicationName'] == 'Terminal'

def on_space(event):
    global counter
    if event.name == 'space' and is_terminal_in_focus():
        counter += int(set_amount)


exercise = input("enter exercise: ")
set_amount = input("enter set rep amount: ")

keyboard.on_press(on_space)

try:
    while True:
        if(is_terminal_in_focus()):
            elapsed_time = (time.time() - start_time) - unfocused_time
            sys.stdout.write("\033[K")  # Clear the line
            print("Time elapsed:", round(elapsed_time, 2), "seconds | Counter:", counter, end="\r")
        else:
            unfocused_time = (time.time() - start_time) - elapsed_time

        time.sleep(1)  # Sleep for a second to avoid high CPU usage
except KeyboardInterrupt:
    print("")

    with open('repcounter.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date.today(), exercise, round(elapsed_time, 2), counter])
        
    pass