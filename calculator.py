def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Calculator")
print("1 Add")
print("2 Substract")
print("3 Multiply")
print("4 Divide\n")

option = int(input('Choose one of the calculations above: '))
while option < 1 or option > 4:
    option = int(input('Pleae enter the correct number for calculation: '))
print(option)

number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))

if option == 1:
    print(add(number1, number2))
elif option == 2:
    print(substract(number1, number2))
elif option == 3:
    print(multiply(number1, number2))
elif option == 4:
    print(divide(number1, number2))
else:
    print('Something wrong...')