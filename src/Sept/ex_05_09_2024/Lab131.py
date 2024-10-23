# Hierarchical Inheritance

class Father:
    def bhk1(self):
        print("1BHK")


class Prashant(Father):
    def bhk2(self):
        print("2BHK")


class Raj(Father):
    def bhk3(self):
        print("3BHK")


class Lucky(Father):
    def no_house(self):
        print("No House")


prashat = Prashant()
prashat.bhk1()
prashat.bhk2()

raj = Raj()
raj.bhk3()
raj.bhk1()