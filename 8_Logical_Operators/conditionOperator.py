num = 5
num2 = 6

a = 6
b = 7
age = 25
temperature = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")

print("EVEN" if num2 % 2 == 0 else "ODD")

max = a if a > b else b
min = a if a < b else b
print(max)
print(min)

status = "Adult" if age >= 18 else "Child"
print(status)

weather = "Hot" if temperature > 20 else "Cold"
print(weather)

access = "Full Access" if user_role == "admin" else "Limited Access"
print(access)