txt_data = "I Like Pizza"

file_path = "d:\\ISRDC\\Python_Brocode\\42_Writing_Files\\Txt\\append.txt"

# w - write
# x - write, if there is no file it will create, if it does we recieve an error
# a - append
# r - read
try:
    with open(file=file_path, mode="a") as file:
        file.write("\n" + txt_data)
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("This file already exists!")