import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_clip(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_clip(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_clip(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_clip(SAVED_DATA, data)
        print("Clipboard data saved")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Clipboard data copied")
        else:
            print("Key does not exist")
    elif command == "list":
        print(data)
    else:
        print("Not a command")
else:
    print("Must be only one command")

# TODO delete key's