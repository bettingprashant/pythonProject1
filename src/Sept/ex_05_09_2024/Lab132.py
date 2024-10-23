# Hybrid Inheritance
class A:
    def methodA(self):
        return "Method A"
class B(A):
        def methodB(self):
            return "Method B"
class C(A):
        def methodC(self):
            return "Method C"

class D(B,C):
    def method(self):
        return "Method D"


