num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter Operator: ")

if op == '+':
    print(f"{num1} + {num2} = {num1 + num2} ")
elif op == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == '/':
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print('Invalid operator')
