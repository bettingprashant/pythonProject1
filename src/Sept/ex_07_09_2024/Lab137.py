
class GrandFather:
    x = 10
    def home(self):
        print("Old  Home")
class Father(GrandFather):
    a = 10
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):
    b = 10
    def home(self):
        super().home()
        print(super().a)
        print("No House")
        print(self.b)

pramod  = Son()
pramod.home()
print(pramod.x)