# Sky PC Automated Music Player

Automate music playback in *Sky: Children of the Light* for the **PC** version using a custom Arduino-powered macro keyboard and a Python script. This script reads music sheets in JSON format and simulates keypresses to play music in-game automatically.

> ⚠️ This version is for PC only and does **not** use Chiaki or remote play.

---

## About

This project allows automated music playback in *Sky: Children of the Light* (PC). It simulates physical keyboard input via an Arduino Micro.

- Reads music sheets (in `.json` format)
- Maps song notes to keyboard inputs
- Sends keypresses using a physical Arduino Micro
- Enables hands-free music playback while your character plays automatically

This version is inspired by a similar tool for Playstation but is specifically built for PC by sending direct input to your keyboard via Arduino HID.

---

## Arduino Setup

You'll need:

- **Arduino Micro** or any board that supports HID (Human Interface Device)
- Arduino IDE installed
- USB-C cable

### Flashing the Arduino

1. Open `auto_player.ino` in Arduino IDE.
2. Set board to **Arduino Micro**  
   `Tools ▸ Board ▸ “Arduino Micro”`
3. Set the correct COM port  
   `Tools ▸ Port ▸ (pick the one labeled Arduino Micro)`
4. Click **Upload** to flash the sketch to the Arduino.

---

## Python Setup

1. Clone this repo or download the files.

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Prepare a song in JSON format.

4. Update the `key_mapping` in the script if your in-game layout differs.

---

## Usage

1. Connect your Arduino Micro to the PC via USB.
2. Launch *Sky: Children of the Light* and enter a musical instrument.
3. Run the Python script:

    ```bash
    python script.py songnamehere
    ```

4. The Arduino will handle keypress playback automatically.

---

## Notes

- You can change the layout mapping inside the Python script:

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

- Ensure your game is focused and accepts keyboard input.
- Tempo and timing is calculated based on note durations in the JSON file.

---

## Other

This script is a fork of a concept originally built for PS4/PS5 users using Chiaki. That version relied on virtual keypresses sent via the Chiaki remote play protocol. This version removes all remote play dependencies by sending real keyboard input using an Arduino Micro.

---

Enjoy the music!
