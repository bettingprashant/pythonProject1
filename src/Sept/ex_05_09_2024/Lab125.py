#Multilevel Inheritance
class Parent:
    gold = "2kg"
    def BHK2(self):
        print("2BHK")
class Child(Parent):
    Diamond = "1kg"
    def BHK3(self):
        print("3BHK")

child_object = Child()
print(child_object.gold)
child_object.BHK3()
child_object.BHK2()

father_object_ref = Parent()
father_object_ref.BHK2()
# father_object_ref.BHK3()
print(child_object.Diamond)

# class ClassValue:
#     a = 10
#
#     def sumvalue(self):
#         print(20+30)
#
# objectvalue = ClassValue()
# objectvalue2 = ClassValue()
# print(objectvalue2.a)
# print(objectvalue.a)
# objectvalue2.sumvalue()
# objectvalue.sumvalue()