#Composition is a concept that models a has a relationship.
#It enables creating complex types by combining objects of other types.
#This means that a class Composite can contain an object of another class Component.
#This relationship means that a Composite has a Component.
#--------------------------------------------------------------------------------------------

class A:
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
          
    def displayA(self):
        print(self.a1)
        print(self.a2)
          
class B:
    def __init__(self,a1,a2,b1,b2):
        self.var = A(a1,a2)
          
        self.b1 = b1
        self.b2 = b2
          
    def displayB(self):
        print(self.var.a1)
        print(self.var.a2)
        print(self.b1)
        print(self.b2)
          
obj = B(11,12,21,22)
print(obj.var.a1)
obj.var.displayA()
obj.displayB()
