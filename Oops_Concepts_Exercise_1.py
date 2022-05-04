"""
1.	Create Calculator using OOPs concept which allows user to perform basic operations
(Addition, Subtraction, Multiplication and Division)
"""


class Calculator:

    global action
    action = input("Enter the action you would like to perform(Addition, Subtraction, Multiplication, Division): ")

    def addition(self, a, b):
        add = a + b
        print("Addition of {} and {} is: {}".format(a, b, add))

    def subtraction(self, a, b):
        sub = a - b
        print("Subtraction of {} and {} is: {}".format(a, b, sub))

    def multiplication(self, a, b):
        mul = a * b
        print("Division of {} and {} is: {}".format(a, b, mul))

    def division(self, a, b):
        div = a / b
        print("Division of {} and {} is: mul".format(a, b, div))


cal = Calculator()

if action == "Addition":
    cal.addition(int(input("Enter value of a:")), int(input("Enter value of b:")))
elif action == "Subtraction":
    cal.substraction(int(input("Enter value of a:")), int(input("Enter value of b:")))
elif action == "Multiplication":
    cal.multiplication(int(input("Enter value of a:")), int(input("Enter value of b:")))
elif action == "Division":
    cal.division(int(input("Enter value of a:")), int(input("Enter value of b:")))


