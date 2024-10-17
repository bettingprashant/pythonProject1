def greet():
    print("Hello world")

result = greet()
print(result)


def greet_by_name(name):
    print("Hello,",name)

greet_by_name("Pramod")



def say_hello_default_arg(name="Pramod"):
    print("Hello",name.upper())

say_hello_default_arg("Amit")
say_hello_default_arg()
say_hello_default_arg(name="Tushar")


def multiple_args(name1="Arpita", name2="Pramod", name3="Amit"):
    print("Multiple Arguments", name1, name2, name3)

multiple_args(name1="Ram",name2="Yunus",name3="Siri")
multiple_args(name1="Ram")


def sum_of_two_number(num1,num2):
    return num1+num2

def sum_of_two_number_with_default(num1=100,num2=200):
    return num1+num2

result = sum_of_two_number(10,34)
result = sum_of_two_number(num1=34,num2=34)
result = sum_of_two_number_with_default()
print(result)