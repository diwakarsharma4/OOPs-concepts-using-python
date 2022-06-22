#Inheritance provides reusability of a code. We don’t have to write the same code again and again.
#It allows us to add more features to a class without modifying it.

class A:
    a1 = 6
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
             
    def check(self):
        print(self.a1)
        A.a1 += 2
        self.a1 = self.a1-1
        print(self.a1)
        print(A.a1)
     
    def get(self):
        return self.a1
             
    def set(self,a1):
        self.a1 = a1
             
class B(A):
    def __init__(self,a1,a2,b1,b2):
        super().__init__(a1,a2)
#         or we can also send variables to class A as--> A.__init__(self,a1,a2)
 
 
        self.a1 = 5
        self.b1 = b1
        self.b2 = b2
              
    def display(self):
        print(self.a1)
        print(self.get(),obj.get())
        print(self.a2)
        print(self.b1)
        print(self.b2)
             
obj = A(2,4)
obj.check()
print(obj.a1)
obj1 = B(1,2,3,4)
obj1.display()
print(obj1.a1,obj1.b1)
print(obj.a1,A.a1)


#obj is the instance created for the class A. It invokes the __init__() of the referred class.
#In Python, every class inherits from a built-in basic class called "object".
#The constructor i.e. the "__init__" function of a class is invoked when we create an object variable or an instance of the class.
#The variables defined within __init__() are called as the instance variables or objects.
#If you forget to invoke the __init__() of the parent class then its instance variables would not be available to the child class. 
