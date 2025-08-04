import serial
import time
import json
import sys

# Open the serial connection (replace 'COM3' with your actual Arduino port)
ser = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

# Chiaki Key Mappings (keep these)
key_mapping = {
    '1Key0': 'y',   # Use physical key Y
    '1Key1': 'u',   # U
    '1Key2': 'i',   # I
    '1Key3': 'o',   # O
    '1Key4': 'p',   # P
    '1Key5': 'h',   # H
    '1Key6': 'j',   # J
    '1Key7': 'k',   # K
    '1Key8': 'l',   # L
    '1Key9': ';',   # ;
    '1Key10': 'n',  # N
    '1Key11': 'm',  # M
    '1Key12': ',',  # ,
    '1Key13': '.',  # .
    '1Key14': '/'   # /
}

def play_music(json_data):
    song_notes = json_data[0]['songNotes']
    bpm = json_data[0]['bpm']
    beat_duration = 60.0 / bpm
    start_time = time.perf_counter()

    for i, note in enumerate(song_notes):
        note_time = note['time']
        note_key = note['key']

        if note_key in key_mapping:
            ser.write(key_mapping[note_key].encode())
        else:
            print("Skipped: Key not found")

        elapsed_time = time.perf_counter() - start_time

        if i < len(song_notes) - 1:
            next_note_time = song_notes[i + 1]['time']
            wait_time = (next_note_time - note_time) / 1000
            remaining_time = max(0, note_time / 1000 + wait_time - elapsed_time)
            time.sleep(remaining_time)

    # Optional: signal end of song
    time.sleep(2)
    ser.write(b't')

if len(sys.argv) > 1:
    song_file = sys.argv[1]
    try:
        with open(f'songs/{song_file}.json', 'r') as file:
            json_data = json.load(file)
        play_music(json_data)
    except FileNotFoundError:
        print("Song not found.")
else:
    print("No song specified.")