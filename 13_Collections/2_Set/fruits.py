# Sets - Unordered and Immutable, but add/remove Ok (NO DUPLICATE) 

fruits = {"apple", "orange", "banana", "coconut", "coconut"}

print(fruits)

for fruit in fruits:
    print(fruit)

# print(dir(fruits))
# print(help(fruits))
print(len(fruits))

print("apple" in fruits)
print("pineapple" in fruits)

fruits.add("pineapple")
fruits.remove("orange")
fruits.pop()

print(fruits)