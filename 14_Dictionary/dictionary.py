capitals = {"USA": "Washiton D.C.",
            "INDIA": "New Delhi",
            "CHINA": "Beijing",
            "RUSSIA":"Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))

if capitals.get("JAPAN"):
    print("That capital exists")
else:
    print("That capital does not exist")

capitals.update({"GERMANY":"Berlin"})
capitals.pop("CHINA")
capitals.popitem()

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

for item in capitals.items():
    print(item)

for key, value in capitals.items():
    print(f"{key}: {value}")