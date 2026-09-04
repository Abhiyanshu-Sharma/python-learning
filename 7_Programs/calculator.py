operator = input("Enter an operator (+ - * /): ")
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

if operator == "+":
    result = n1 + n2
    print(round(result, 3))
elif operator == "-":
    result = n1 - n2
    print(round(result, 3))
elif operator == "*":
    result = n1 * n2
    print(round(result, 3))
elif operator == "/":
    result = n1 / n2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator")