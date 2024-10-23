print("---Start of the Program---")
try:
    a = int(input("Enter the num 1"))
    b = int(input("Enter the num 2"))
    c = a / b
    print("Result DIv is ", c)
except Exception as e:
    print(e)
    print("Please check your inputs,it shouldn't be a string or zero")
print("---End of the Program---")