# Considered Bad Practice

try:
    n = int(input("Enter a Number: "))
    print(1 / n)
except Exception:
    print("Something Went Wrong!")