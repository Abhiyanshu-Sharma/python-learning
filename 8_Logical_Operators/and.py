temperature = 25
is_sunny = True

if temperature >= 28 and is_sunny:
    print("It is Hot outside 🥵")
    print("It is Sunny 🌞")
elif temperature <= 0 and is_sunny:
    print("It is Cold outside ❄️")
    print("It is Sunny 🌞")
elif temperature < 28 and is_sunny:
    print("It is Cold outside ❄️")
    print("It is Sunny 🌞")