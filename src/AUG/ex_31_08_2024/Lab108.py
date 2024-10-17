class Dog:
    name = "Tommy"
    breed = None
    color = None


    def sleep(self):
        print("Sleeping")
    def bark(self):
        print("bark")

dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()