#Ex 1

# print("This is starting point of program....")
# print("This is starting point of program....")
# print("This is starting point of program....")
#
# try:
#     print(x)
# except:
#     print("Exception occured")
#
#
#
# print("This is end point of program...")
# print("This is end point of program...")
# print("This is end point of program...")

#Ex 2

# print("This is starting point of program....")
# print("Program is in progress")
#
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("exception occured and handled")
#
# print("program complted")

#example 3 Multiple step blocks
# try:
#     num1, num2 = 10, 5
#     result = num1 / num2
#     print("result is :", result)
#
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception... ")
# except SyntaxError:
#     print("Thrown syntax error exception...")
# except:
#     print("Exception handled...")
# else:
#     print("No exception occured...")
# finally:
#     print("always execute")

#example 4 raising our own exception

def enterage(num):
    if num<0:
        raise ValueError ("only integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")

print("checking number is even or add by calling function..")
num=-1
try:
    enterage(-1)
except ValueError:
    print("exception occured and handled")
print("Program completed")



