import keyboard, subprocess, os, time, importlib
import pygetwindow
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Controller as KeyboardController, Key
import threading
import pyautogui

# ----------------------------------------------------------------
# Use the code below to create an exe. Place it in a file and edit 
# ----------------------------------------------------------------
# import PyInstaller.__main__
# PyInstaller.__main__.run([
#    '{script_name}.py',
#    '--onefile',
#    '--windowed',
#    "--icon={icon_name}.ico"
# ])
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# Install a new pip package
# ----------------------------------------------------------------
def install_pip_package(package_name):
    importlib.import_module(package_name)

# ----------------------------------------------------------------
# Install all the packages needed to run all functions in this file
# ----------------------------------------------------------------
def install_pip_packages():
    install_pip_package('pygetwindow')
    install_pip_package('pynput')
    install_pip_package('pyautogui')

# ----------------------------------------------------------------
# Run an exectuable/shortcut or pretty much any file
# NOTE: This will start it without running as admin and you won't
# be able to use the keyboard and mouse imports to automate this
# ----------------------------------------------------------------
def open_executable(exe_path):
    os.startfile(exe_path)

# ----------------------------------------------------------------
# Run a command and get the ouput. By default the command will be run
# in your current directory, but you can change it to run somewhere else
# ----------------------------------------------------------------
def run_command(command, directory=None):
    if directory is None:
        results = subprocess.run(command, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        results = subprocess.run(f'cd {directory} && {command}', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    out = results.stdout
    err = results.stderr
    return out, err

# ----------------------------------------------------------------
# Open a new cmd window and run a command
# ----------------------------------------------------------------
def run_command_in_window(command, directory=None):
    if directory is None:
        subprocess.Popen(f'start cmd /k {command}', shell=True)
    else:
        
        subprocess.Popen(f'cd {directory} && start cmd /k {command}', shell=True)

# ----------------------------------------------------------------
# Open a new process as an admin user
# NOTE: A request for admin privileges may popup, you might have to find
# a way around that
# ----------------------------------------------------------------
def run_process_as_admin(abs_path_to_shortcut):
    powershell_command = f"Start-Process '{abs_path_to_shortcut}' -Verb RunAs"
    subprocess.run(["powershell", "-Command", powershell_command])

# ----------------------------------------------------------------
# Log into something. This will do the standard login where you enter
# the username, press tab to enter the password, then press enter to 
# finalize login.
# remember_me_option_available -- This is used for that checkbox that says
# "remember me". It will automatically check that box if this option is set to 
# true. (Depending on the website, you may have to change the number of
# of times that tab is pressed to get to it)
def login(username, password, remember_me_option_available=False):
    if username is None or password is None:
        raise Exception("Please enter a username and password.")
    keyboard.write(username)
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.write(password)
    time.sleep(.25)
    if remember_me_option_available:
        keyboard.press_and_release('tab')
        time.sleep(.25)
        keyboard.press_and_release('space')
        time.sleep(.25)
    keyboard.press_and_release('enter')

# ----------------------------------------------------------------
# Open a list of URLS in the browser of your choice
# ----------------------------------------------------------------
def open_urls(browser_name, url_list, browser_load_time=2.5):
    if not focus_window(browser_name):
        subprocess.run(f'start {browser_name}', shell=True)
        time.sleep(browser_load_time)
    for url in url_list:
        keyboard.press_and_release('ctrl+t')
        time.sleep(.25)
        keyboard.press_and_release('ctrl+e')
        time.sleep(.25)
        keyboard.press_and_release('backspace')
        time.sleep(.25)
        keyboard.write(url)
        time.sleep(.5)
        keyboard.press_and_release('enter')
        time.sleep(.5)

# ----------------------------------------------------------------
# Close all your windows that aren't settings or blackground tasks
# ----------------------------------------------------------------
def close_all_windows():
    windows = pygetwindow.getAllWindows()
    for window in windows:
        if window.title != "" and window.title != "Settings":
            window.close()

# ----------------------------------------------------------------
# Close a specific window
# ----------------------------------------------------------------
def close_window(window_name):
    windows = pygetwindow.getWindowsWithTitle(window_name)
    if len(windows) > 0:
        windows[0].close()

# ----------------------------------------------------------------
# Focus on a specific window
# ----------------------------------------------------------------
def focus_window(window_name):
    windows = pygetwindow.getWindowsWithTitle(window_name)
    if len(windows) > 0:
        windows[0].activate()
        return True
    else:
        return False

# ----------------------------------------------------------------
# Build a long series of commands in the following format:
# <cmd1> && <cmd2> && <cmd3>
# This will allow you to pass it to another method that executes all of them
# ----------------------------------------------------------------
def build_series_of_commands(commands):
    output_cmd = ""
    for i, input_cmd in enumerate(commands):
        output_cmd += input_cmd
        if i != len(commands) - 1:
            output_cmd += " && "
    return output_cmd

# ----------------------------------------------------------------
# Delete a file
# ----------------------------------------------------------------
def delete_file(file_path):
    os.remove(file_path)

# ----------------------------------------------------------------
# Make a new folder
# ----------------------------------------------------------------
def make_folder(folder_name, directory=None):
    if directory is None:
        directory = os.path.dirname(__file__)
    os.mkdir(directory + f'/{folder_name}')

# ----------------------------------------------------------------
# Record input and save it to a file, this will log all of your
# key presses, mouse clicks, and scrolls.
# NOTE: For some reason, this cannot do keybinds
# ----------------------------------------------------------------
def record_input(save_location, duration=15):
    events = []
    if os.path.exists(save_location):
        delete_file(save_location)
    # On Click, log it

    def on_click(x, y, button, pressed):
        if pressed:
            events.append((f'Mouse Press: {x},{y},{button}'))
        else:
            events.append((f'Mouse Release: {x},{y},{button}'))

    def on_press(key):
        try:
            events.append(f'Key Press: {key.char}')
        except AttributeError:
            events.append(f'Key Press: {key}')

    def on_release(key):
        try:
            events.append(f'Key Release: {key.char}')
        except AttributeError:
            events.append(f'Key Release: {key}')

    # On scroll, log it
    def on_scroll(x, y, dx, dy):
        events.append(f'Mouse scroll: {x},{y},{dy}')

    # Start the listener threads to check for scrolls, clicks, and presses
    with MouseListener(on_click=on_click, on_scroll=on_scroll) as mouse_listener, KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        threading.Timer(duration, mouse_listener.stop).start()
        threading.Timer(duration, keyboard_listener.stop).start()
        try:
            mouse_listener.join()
            keyboard_listener.join()
        except KeyboardInterrupt:
            pass
    # Save the logs to a recording file
    with open(save_location, 'w') as recording_file:
        for event in events:
            recording_file.write(event + "\n")

def get_events_from_recording(recording_file):
    events = []
    # Parse the recording file and put it in a format that we can use for the controllers
    with open(recording_file, 'r') as recording_file:
        lines = recording_file.readlines()
        for line in lines:
            # Remove new lines
            line = line.replace("\n", "")
            # If the current event is mouse click
            if "Mouse Press" in line:
                # Parse the locations and type of click out
                line = line.replace("Mouse Press: ", "")
                split_line = line.split(',')
                x, y, str_button = int(split_line[0]), int(split_line[1]), split_line[2]
                str_button = str_button.replace("Button.", "")
                # Store the values
                events.append(('mouse_press', (x, y, str_button)))
            # If the current event is a mouse release
            elif "Mouse Release" in line:
                # Parse the locations and type of the mouse release
                line = line.replace("Mouse Release: ", "")
                split_line = line.split(',')
                x, y, str_button = int(split_line[0]), int(split_line[1]), split_line[2]
                str_button = str_button.replace("Button.", "")
                # Store the values
                events.append(('mouse_release', (x, y, str_button)))
            # If the current event is a key press
            elif "Key Press" in line:
                # Parse the type of key press
                pressed_key = line.replace("Key Press: ", "")
                if pressed_key == "None":
                    continue
                # If it is a special character (Key.shift), get the type of key and store it
                if 'Key.' in pressed_key:
                    pressed_key = pressed_key.replace("Key.", "")
                    pressed_key = Key[pressed_key]
                events.append(('key_press', (pressed_key)))
            elif "Key Release" in line:
                # Parse the type of key press
                released_key = line.replace("Key Release: ", "")
                if released_key == "None":
                    continue
                # If it is a special character (Key.shift), get the type of key and store it
                if 'Key.' in released_key:
                    released_key = released_key.replace("Key.", "")
                    released_key = Key[released_key]
                events.append(('key_release', (released_key)))
            # If the current event is a scroll
            elif "Mouse scroll" in line:
                # Check which type of scroll and store it
                split_line = line.replace("Mouse scroll: ", "").split(",")
                x, y, scroll = int(split_line[0]), int(split_line[1]), int(split_line[2])
                events.append(('scroll', (x, y, scroll)))
    return events

# ----------------------------------------------------------------
# Function for replaying a recording file made by the record_input() method
# scroll_level -- changes how many pixels are scrolled each time
# NOTE: You must start at the same place you took the recording.
# ----------------------------------------------------------------
def replay_recording(recording_file, scroll_level=100):
    events = get_events_from_recording(recording_file)
    for i in reversed(range(3)):
        print(f'Recording starting in {i + 1} seconds...')
        time.sleep(1)
    keyboard_controller = KeyboardController()
    # Replay the events
    for event in events:
        # Get event type (mouse, key, scroll)
        event_type = event[0]
        if event_type == "mouse_press":
            # Go to click location and use the correct mouse button
            x, y, input_button = event[1]
            pyautogui.mouseDown(x=x, y=y, button=input_button)
            time.sleep(.1) # Sleep for .1 to give the computer time to catch up
        elif event_type == "mouse_release":
            # Go to release location and use the correct mouse button
            x, y, input_button = event[1]
            pyautogui.dragTo(x=x, y=y, button=input_button, duration=.5)
            pyautogui.mouseUp()
            time.sleep(.1) # Sleep for .1 to give the computer time to catch up
        elif event_type == 'key_press':
            # Press the proper key
            pressed_key = event[1]
            try:
                keyboard_controller.press(pressed_key)
            except:
                print(f'Error: Key "{pressed_key}" not found')
            time.sleep(.05) # Sleep for .05 to give the computer time to catch up
        elif event_type == 'key_release':
            # Press the proper key
            pressed_key = event[1]
            keyboard_controller.release(pressed_key)
            time.sleep(.05) # Sleep for .05 to give the computer time to catch up
        elif event_type == 'scroll':
            # Get the direction and scroll
            x, y, scroll = event[1]
            pyautogui.moveTo(x, y)
            pyautogui.scroll(scroll * scroll_level)
            time.sleep(.025) # Sleep for .1 to give the computer time to scroll properly. (Using .025 instead of .1 because it is smoother)
