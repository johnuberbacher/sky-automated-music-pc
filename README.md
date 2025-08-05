# Sky PC Automated Music Player

Automate music playback in Sky: Children of the Light (PC) using an Arduino Micro and a Python script with a simple graphical interface. The script reads JSON-formatted songs and sends keypresses via Arduino HID to simulate live music input.

---

### Requirements

- **Arduino Micro** (or any HID-compatible board)
- **Arduino IDE**
- **Python 3.8+**
- USB cable

---

## Arduino Setup

1. Open `sketch_aug3a.ino` in Arduino IDE.
2. Set board:  
   `Tools ▸ Board ▸ “Arduino Micro”`
3. Set port:  
   `Tools ▸ Port ▸ (your Arduino Micro)`
4. Click **Upload** to flash.

---

### Python Setup

1. Clone or download this repo.
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    pip install pywin32  # For Windows window focusing
    ```

3. Prepare a song file (`.json` format).
4. Adjust `key_mapping` in `script.py` if needed:

    ```python
    key_mapping = {
        '1Key0': '3',
        '1Key1': '4',
        '1Key2': 'k',
        '1Key3': 'x',
        '1Key4': 'j',
        '1Key5': 'v',
        '1Key6': 'i',
        '1Key7': 'z',
        '1Key8': 'l',
        '1Key9': 'c',
        '1Key10': '1',
        '1Key11': '2',
        '1Key12': 'a',
        '1Key13': 'j',
        '1Key14': 'd'
    }
    ```

---

### Usage

1. Plug in the Arduino.
2. Launch *Sky* and open an instrument.
3. Run the script

---

### Notes

- The script tries to focus the game window (by exact title match) before sending input. Make sure your game is running and the window title matches the configured name (default: "Sky: Children of Light").
- Only one song can play at a time; starting a new song stops the previous one.
- The GUI handles song selection and playback; no command-line song argument is needed anymore.
- Song tempo and note timings are based on the JSON files in the songs/ folder.
- Uses Windows-specific pywin32 for window focusing; Linux/macOS are not supported.
- The Arduino sends real keypresses; no virtual input or remote play involved.
