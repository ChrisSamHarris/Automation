#Multi-clipboard Python Script - Controls clipboard to hold 3 values at any time 
# Currently broken !!
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

#print(data)
# one or more synchronization tasks are not valid

#clipboard.copy("abc")
# ==== IF NOT PROCEEDING FURTHER - Paste here: ** In this case it should paste "abc" 

#print(sys.argv[1:]) #Use this command with "python3 multiclip.py hello world" and see what is print
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

#save_items("test.json", {"key":"value"})

def load_data(filepath):
    try: 
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except: 
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    #print(command)
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data has been copied to clipboard.")
        else:
            print('Key does not exist!')
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.") #Python3 multiclip.py <Command>