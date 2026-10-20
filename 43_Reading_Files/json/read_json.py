import json

file_path = "D:\\ISRDC\\Python_Brocode\\42_Writing_Files\\json\\dictionary_dump.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read that file")