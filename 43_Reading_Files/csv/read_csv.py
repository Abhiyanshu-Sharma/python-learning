import csv

file_path = "D:\\ISRDC\\Python_Brocode\\42_Writing_Files\\csv\\list_of_list.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read that file")