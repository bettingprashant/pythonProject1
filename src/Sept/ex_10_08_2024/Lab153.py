try:
    num1 = int(input("Enter the num1\n"))
    num2 = int(input("Enter the num2\n"))
    result = num1/num2
except ValueError as ve:
    print("Enter the value in Int")
except ZeroDivisionError as zde:
    print("Num2 shouldn't be zero")
else:
    print("Result is ",result)
finally:
    print("This code will be alwways executed")
