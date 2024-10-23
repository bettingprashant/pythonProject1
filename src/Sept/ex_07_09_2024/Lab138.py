class MathUtils(object):
    def add(self,a,b):
        return a + b

    def add(self, a,b,c=0):
        return a + b + c
    def add(self,a,b,c=10,d=1):
        return a+b+c+d

math = MathUtils()
op1 = math.add(1,2)
print(op1)
