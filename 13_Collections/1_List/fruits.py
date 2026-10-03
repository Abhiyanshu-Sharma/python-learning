# Lists - Ordered and Changeable (Duplicates OK) 

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)
print(fruits[0])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])

# print(fruits[4]) 
# IndexError: list index out of range

for fruit in fruits:
    print(fruit)

# print(dir(fruits))
# print(help(fruits))
print(len(fruits))

print("apple" in fruits)
print("pineapple" in fruits)

# fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("orange")
fruits.insert(0, "kiwi")
fruits.sort()
fruits.reverse()
print(fruits.index("apple"))
print(fruits.count("pineapple"))
# fruits.clear()

print(fruits)