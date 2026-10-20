try:
    n = int(input("Enter a Number: "))
    print(1 / n)
except ZeroDivisionError:
    print("You can't divide by zero Idiot!")
except ValueError:
    print("Enter only Numbers please")