temperature = 28
is_sunny = False

if temperature >= 28 and not is_sunny:
    print("It is Hot outside 🥵")
    print("It is Sunny 🌞")
elif temperature <= 0 and not is_sunny:
    print("It is Cold outside ❄️")
    print("It is Sunny 🌞")
elif temperature < 28 and not is_sunny:
    print("It is Cold outside ❄️")
    print("It is Sunny 🌞")