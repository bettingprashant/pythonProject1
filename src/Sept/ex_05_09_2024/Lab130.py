
class GrandParent:
    key_gold = "1kg"
    def grandparent_method(self):
        return "GrandParent's Method"
class Parent(GrandParent):
    def parent_method(self):
        return "Parent's Method"
    
class Child(Parent):
    mac_m3_apple = "M3 Max"
    def child_method(self):
        return "Child's Method"

child = Child()
print(child.grandparent_method())

