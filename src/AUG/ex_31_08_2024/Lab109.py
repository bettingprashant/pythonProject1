class Dog:

    name =  None
    age = None

    def __init__(self,name,age):
        print("called, Object is created")
        self.name = name
        self.age = age
    def sleep(self):
        print("Sleeping")
        print("who is sleeping ->"+ self.name)

dog1 = Dog("chow", 10)
print(dog1.name)
dog1.sleep()

dog2 = Dog("mow",20)
print(dog2.name)
dog2.sleep()
