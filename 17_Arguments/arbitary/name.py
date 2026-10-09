def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Spongebob", "Sqarepants")
print()
display_name("Spongebob", "Harold", "Sqarepants")
print()
display_name("Dr.", "Spongebob", "Harold", "Sqarepants")
print()
display_name("Dr.", "Spongebob", "Harold", "Sqarepants", "III")