# Taking input from User

class Person:
    def __init__(self):
        self.name = input("Enter the name \n")
        self.age = input("Enter the age \n")
        self.phone = input("Enter the phone \n")
        self.occupation = input("Enter the occupation \n")

    def name_of_the_function(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone is {self.phone}")
        print(f"Occupation is {self.occupation}")

person1 = Person()

person1.name_of_the_function()