import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job":"cook"
}

file_path = "d:\\ISRDC\\Python_Brocode\\42_Writing_Files\\json\\dictionary_dump.json"

try:
    with open(file=file_path, mode="w") as file:
        json.dump(employee, file, indent=4)
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("This file already exists!")