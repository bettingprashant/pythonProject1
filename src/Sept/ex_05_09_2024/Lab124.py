#Single Inheritance

class Father:
    key = "2BHK"

    def car(self):
        print("Father  Car!!", "ALTO")
        print("Father Car!!", "ALTO", self.key)

class Son(Father):
    pass

father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.car()