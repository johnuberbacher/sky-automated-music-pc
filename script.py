import serial
import time
import json
import sys
import threading
import tkinter as tk
from tkinter import ttk
import win32gui
import win32con
import os

# Open the serial connection (adjust port as needed)
ser = serial.Serial("COM8", 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

# Chiaki Key Mappings
key_mapping = {
    "1Key0": "y",
    "1Key1": "u",
    "1Key2": "i",
    "1Key3": "o",
    "1Key4": "p",
    "1Key5": "h",
    "1Key6": "j",
    "1Key7": "k",
    "1Key8": "l",
    "1Key9": ";",
    "1Key10": "n",
    "1Key11": "m",
    "1Key12": ",",
    "1Key13": ".",
    "1Key14": "/",
}

# Globals for controlling playback
playback_thread = None
stop_event = threading.Event()


def focus_game_window(window_title_exact="Sky"):
    def enum_callback(hwnd, results):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title.lower() == window_title_exact.lower():
                results.append(hwnd)

    results = []
    win32gui.EnumWindows(enum_callback, results)
    if results:
        hwnd = results[0]
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        return True
    return False


def play_music(json_data):
    song_notes = json_data[0]["songNotes"]
    bpm = json_data[0]["bpm"]
    beat_duration = 60.0 / bpm
    start_time = time.perf_counter()

    for i, note in enumerate(song_notes):
        if stop_event.is_set():
            # Stop immediately if stop event triggered
            return

        note_time = note["time"]
        note_key = note["key"]

        if note_key in key_mapping:
            ser.write(key_mapping[note_key].encode())
        else:
            print("Skipped: Key not found")

        elapsed_time = time.perf_counter() - start_time

        if i < len(song_notes) - 1:
            next_note_time = song_notes[i + 1]["time"]
            wait_time = (next_note_time - note_time) / 1000
            remaining_time = max(0, note_time / 1000 + wait_time - elapsed_time)
            # Instead of sleep all at once, break it up to respond to stop_event
            waited = 0
            while waited < remaining_time:
                if stop_event.is_set():
                    return
                sleep_chunk = min(0.05, remaining_time - waited)
                time.sleep(sleep_chunk)
                waited += sleep_chunk

    # Optional: signal end of song
    time.sleep(2)
    ser.write(b"t")


def start_song():
    global playback_thread

    # If a song is already playing, stop it first
    if playback_thread and playback_thread.is_alive():
        stop_event.set()
        playback_thread.join()  # wait for previous thread to finish

    stop_event.clear()

    # Try to focus game window, ignore if fails
    focused = focus_game_window()
    if not focused:
        print("Game window not found or couldn't be focused")

    song_name = song_var.get()
    if not song_name:
        print("No song selected.")
        return

    try:
        with open(f"songs/{song_name}.json", "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print("Song not found.")
        return

    playback_thread = threading.Thread(
        target=play_music, args=(json_data,), daemon=True
    )
    playback_thread.start()


def stop_song():
    stop_event.set()
    # Optional: send a signal to Arduino to stop any current input
    ser.write(b"s")  # For example, you can define 's' as stop on Arduino side


def center_window(win, width=400, height=200):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")


# Tkinter GUI setup
root = tk.Tk()
root.title("Sky: Music Player")

frame = ttk.Frame(root, padding=20)  # less padding than 20 if you want it tighter
frame.pack(fill="both", expand=True)

# Load song list
songs_folder = "songs"
song_files = [f[:-5] for f in os.listdir(songs_folder) if f.endswith(".json")]

tk.Label(frame, text="Select a song:").pack(
    pady=(0, 2), anchor="w"
)  # very little vertical space, left aligned

song_var = tk.StringVar()
song_dropdown = ttk.Combobox(
    frame, textvariable=song_var, values=song_files, state="readonly"
)
song_dropdown.pack(fill="x", pady=(0, 10))  # fill full width, small space below

btn_frame = tk.Frame(frame)
btn_frame.pack(fill="x")

btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)

start_btn = tk.Button(btn_frame, text="Start", command=start_song)
start_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))

stop_btn = tk.Button(btn_frame, text="Stop", command=stop_song)
stop_btn.grid(row=0, column=1, sticky="ew", padx=(5, 0))

center_window(root, 350, 135)
root.mainloop()
