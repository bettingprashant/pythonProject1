#1

# class A:
#     def m1(self):
#         print("This is m1 Method of class A")
#
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
#
# bobj=B()
# bobj.m1()
# bobj.m2()

#2

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x,self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a,self.b)
# bobj=B()
# bobj.m1()
# bobj.m2()

#3

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=300,200
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=40,10
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=C()
# bobj.m1()
# bobj.m2()
# bobj.m3()

#4

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=300,200
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=40,10
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1()
# bobj.m2()
#
# cobj=C()
# cobj.m1()
# cobj.m3()

#5 Multiple Inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=300,200
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=40,10
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

#6

# class A:
#     def m1(self):
#         print("This is m1 Method from A class")
#
# class B(A):
#     def m1(self):
#         print("This is m1 method from B class")
#         super().m1()
#
# bobj=B()
# bobj.m1()

#7

# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
#
# bobj=B()
# bobj.m(1000,2000)

#8  Overriding variables

# class Parent:
#     name="Scott"
#
# cobj=Child()
# print(cobj.name)
#
# class Child(Parent):
#     name="Raj"

#9 Overriding methods

# class Bank:
#     def rateOfInterest(self):
#         return 0
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
#
# objx=XBank()
# print(objx.rateOfInterest())
#
# objy=YBank()
# print(objy.rateOfInterest())

# 10 Overloading 1 (Polymorphism)

# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello"+name)
#         else:
#             print("Hello")
# h=Human()
# h.sayhello("Raj")
# h.sayhello()

#11 Overloading 2

class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

calobj=Calculation()
calobj.add()
calobj.add(10,20)
calobj.add(100,200,300)