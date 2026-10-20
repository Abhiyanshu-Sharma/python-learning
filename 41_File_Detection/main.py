import os

base_path = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_path, "test.txt")
file_path2 = os.path.join(base_path, "test")

print(os.getcwd())

# Check the file
if os.path.exists(file_path):
    print(f"The Location -[ {file_path} ]- Exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a Directory")
else:
    print("Location Does Not Exist")

# Check the directory
if os.path.exists(file_path2):
    print(f"The Location -[ {file_path2} ]- Exists")

    if os.path.isfile(file_path2):
        print("That is a file")
    elif os.path.isdir(file_path2):
        print("That is a Directory")
else:
    print("Location Does Not Exist")