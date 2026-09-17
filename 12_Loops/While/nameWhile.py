name = input("Enter Your Name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Enter Your Name: ")
print(f"Hello {name}")