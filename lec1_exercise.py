# Author: Rasheeq Mohammad
# Date: September 13, 2022
# GNG5300 2022 Lecture 1

print("Enter two numbers")
print("Specify which operation you want")
a = input("Enter number 1: ")
b = input("Enter number 2: ")

a = int(a)
b = int(b)

op = input("Enter operation (+, -, *, **, /): ")

def do_operation(x, y, op):
    result = None
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '**':
        result = x ** y
    elif op == '/':
        try:
            result = x / y
        except ZeroDivisionError:
            print("Cannot divide by 0; please restart")
    else:
        print("Did not recognize the operation; please restart")
    return result

result = do_operation(a, b, op)
if result is not None:
    print("Result = %d" % result)
    print("Enter a third number to apply to the operation above")
    c = input("Enter number 3: ")
    c = int(c)
    new_result = do_operation(result, c, op)
    if new_result is not None:
        print("Updated result = %d" % new_result)
    else:
        print("Failed; please restart")
else:
    print("Failed; please restart")
print("END of the program")
