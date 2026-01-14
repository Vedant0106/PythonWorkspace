try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    print("vedant")
    result = number1 / number2
    print("Result:", result)
    print("hello")
except ValueError:
    print("Error: Please enter valid integers")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

finally:
    print("Program execution completed")
