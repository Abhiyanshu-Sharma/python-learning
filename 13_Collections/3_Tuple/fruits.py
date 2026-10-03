# Tuple - Ordered and Unchangeable (Duplicates OK), Faster

fruits = ("apple", "orange", "banana", "coconut", "coconut")

print(fruits)

for fruit in fruits:
    print(fruit)

# print(dir(fruits))
# print(help(fruits))
print(len(fruits))

print("apple" in fruits)
print("pineapple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))


print(fruits)