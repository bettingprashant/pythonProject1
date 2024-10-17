#1

# class Myclass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# mc1=Myclass()
# mc1.myfun()
# mc1.display("Raj")

#2

# class Myclass:
#     def m1(self):
#         print("THis is instance Method")
#     def m2(self,num):
#         print(self,num)
#
# mc=Myclass()
# mc.m1()
# mc.m2(100)
# Myclass.m2(10,20)


#3

# class Myclass:
#     a,b = 10,20
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=Myclass()
# mc.add()
# mc.mul()

#4

# i,j=15,25
# class Myclass:
#     a,b=10,20
#     def add(self,x,y):
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
#
# mc=Myclass()
# mc.add(100,200)

#5

# a,b=15,25
# class Myclass:
#     a,b=10,20
#     def add(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#
#         print(globals()['a']+globals()['b'])
# mc=Myclass()
# mc.add(100,200)

#6

# class Myclass:
#     def display(self,name):
#         print("This is display method")
#         print(name)
#
# obj1=Myclass()
# obj1.display("raj")
#
# obj2=Myclass()
# obj2.display("singh")

#7

# class Myclass:
#     def __init__(self):
#         print("this is a constructor")
#     def m1(self):
#         print("hello..")
#     def m2(self,x,y):
#         return(x+y)
#
# mc=Myclass()
# mc.m1()
# print(mc.m2(10,20))

#8

# class Myclass:
#     name="John"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
# mc=Myclass("David")

#9

# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# e1=Emp(101,"John",500000)
# e1.display()
#
# e2=Emp(102,"Raj",700000)
# e2.display()

#10

class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def __str__(self):
        return(self.ename)

e1=Emp(101,"John",500000)
print(e1)

e2=Emp(102,"Raj",700000)
e2.display()