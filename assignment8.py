# when writing error start with (try) and end with (expect the error)
import math
try:
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")
    operation = input("operation: ")

    if operation == "+":
       print(float(num1) +float(num2))
    elif operation == "-":
         print(float(num1) - float(num2))
    elif operation == "*":
         print(float(num1) * float(num2))
    elif operation == "/":
         print(float(num1) / float(num2))
    elif operation == "//":
         print(float(num1) // float(num2))
    elif operation == "%":
         print(float(num1) % float(num2))
    elif operation == "^":
         print(math.pow(float(num1),float(num2)))
    elif operation == "'":
         print(float(num1) ** (1/float(num2)))
    elif operation == "Log":
         print(math.log(float(num1),float(num2)))

except ZeroDivisionError:
    print("UNDEFINED")
except ValueError:
    print("INVALID INPUT")







