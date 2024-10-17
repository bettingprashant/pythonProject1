class Car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name" + self.name)
        print("Starting a car with the name" + self.make)
        print("Starting a car with the name" + self.model)

lambo = Car("Lambo","V2", "2023")
lambo.start_engine()
xuv = Car("XUV", "V3", "2024")
xuv.start_engine()