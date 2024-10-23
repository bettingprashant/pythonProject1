class Person:
    # class variables
    #Instance variables
    #name = "Raj" Hardcoded value
    def __init__(self,name):
        self.name = name

    def walk(self,name):
            self.name = name

amit = Person("amit")
pramod = Person("pramod")
print(amit.name)
print(pramod.name)