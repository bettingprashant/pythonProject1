# OOPs
# Class - Blueprint
# OBject - Instance of class
# Encapsulation - private__, protected_, public.
# Inheritance - Single, Multilevel, Multiple, Hierarchical, Hybrid
# Polymorphism - method overriding, method overloading(Not supported in Python)
# self,super(), __init__(onstructor)

#Abstraction - It is a fundamental Concept

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name =name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog("NN")
dog.sound()