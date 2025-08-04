# Sky PC Automated Music Player

Automate music playback in *Sky: Children of the Light* (PC) using an Arduino Micro and a Python script. The script reads JSON-formatted songs and sends keypresses via Arduino HID to simulate live music input.

> ⚠️ For PC only. No remote play or Chiaki needed.

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
3. Run the script:

    ```bash
    python script.py songname
    ```

---

### Notes

- Make sure the game window is focused and ready to receive input.
- Song tempo is based on durations in the JSON file.
- Built from the PS version but sends actual keypresses via Arduino—no virtual input or remote play required.
