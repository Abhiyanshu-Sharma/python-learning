employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "d:\\ISRDC\\Python_Brocode\\42_Writing_Files\\Txt\\employees.txt"

# w - write
# x - write, if there is no file it will create, if it does we recieve an error
# a - append
# r - read
try:
    with open(file=file_path, mode="x") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("This file already exists!")