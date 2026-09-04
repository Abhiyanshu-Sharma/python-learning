age = int(input("Enter your age: "))

if age >= 100:
    print("Too old to Signup")
elif age >= 18:
    print("You are above 18, you can Signup")
elif age < 0:
    print("You are not born yet >_<")
else:
    print("You must be 18+ to Signup")