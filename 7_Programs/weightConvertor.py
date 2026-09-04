weight = input("Enter your weight: ")
unit = input("Kilograms or Pounds (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid unit")
    exit()

print(f"Your weight is: {round(weight, 1)} {unit}")