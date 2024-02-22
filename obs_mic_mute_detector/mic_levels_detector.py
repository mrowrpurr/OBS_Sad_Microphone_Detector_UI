import threading
import time as tm
from typing import Callable, Optional

import numpy as np
import sounddevice as sd

RATE = 44100  # Sample rate
CHANNELS = 1  # Mono audio
SILENCE_THRESHOLD = 1.1  # Adjust this based on your microphone sensitivity
SECONDS_OF_SILENCE = 2  # Duration of silence before printing a message

silence_start = None  # Initialize the start time of silence


def print_silence(
    indata: np.ndarray,
    _frames: int,
    _time_info: tuple,
    _status: sd.CallbackFlags,
    silence_callback: Callable,
) -> None:
    global silence_start  # Use the global variable to track silence start time
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm < SILENCE_THRESHOLD:
        if silence_start is None:
            silence_start = tm.time()  # Record the start time of silence
        elif tm.time() - silence_start > SECONDS_OF_SILENCE:
            silence_callback()  # Call the provided callback function
            silence_start = tm.time()  # Reset the start time of silence
    else:
        silence_start = None  # Reset silence_start when noise is detected


def monitor_microphone(device_name: Optional[str], silence_callback: Callable) -> None:
    def callback_wrapper(indata, frames, time, status):
        print_silence(indata, frames, time, status, silence_callback)

    device_id = None
    if device_name:
        # Try to find the device by name
        try:
            device_id = sd.find_device(device_name)
        except ValueError:
            print(f"Device named '{device_name}' not found. Using default.")

    # Define and start the background thread for monitoring
    def monitor_thread():
        with sd.InputStream(
            device=device_id,
            channels=CHANNELS,
            callback=callback_wrapper,
            blocksize=int(RATE * SECONDS_OF_SILENCE / 10),  # Adjust block size
            samplerate=RATE,
        ):
            print("Monitoring microphone... Speak into your microphone.")
            while True:  # Keep the stream alive
                tm.sleep(0.1)

    # Start the background thread
    thread = threading.Thread(target=monitor_thread)
    thread.daemon = (
        True  # Set as a daemon so it automatically closes when the main program exits
    )
    thread.start()


# Example usage:
# def silence_detected():
# print("Silence detected callback triggered.")


# Replace 'Your Device Name Here' with your microphone's device name if needed
# monitor_microphone(None, silence_detected)  # Or put your device name as a string
