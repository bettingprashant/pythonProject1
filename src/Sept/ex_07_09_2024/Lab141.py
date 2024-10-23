from abc import ABC,abstractmethod
class PyATB(ABC):
    @abstractmethod
    def PayFee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Amit(PyATB):
    def PayFee(self):
        print("Paid")


shubham = Amit()
shubham.enrolled()