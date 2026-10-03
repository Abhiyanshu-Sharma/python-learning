fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

groceries2 = [
            ["apple", "orange", "banana", "coconut"],
            ["celery", "carrots", "potatoes"],
            ["chicken", "fish", "turkey"]
        ]

print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[0][2])
print(groceries[2][1])

print(groceries2)

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
