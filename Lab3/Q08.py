try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    sum =  num1/num2
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Incorrect Value")