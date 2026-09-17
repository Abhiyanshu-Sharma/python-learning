age = input("Enter your Age: ")

while age < 0:
    print("Age can't be negative")
    age = input("Enter your Age: ")
print(f"You are {age} year's old")