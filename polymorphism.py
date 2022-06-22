#Poymorphism is the process of having multiple forms for a single entity.
#Python which exclusively works with objects shows polymorphism on objects, which means the objects take multiple forms.
#Polymorphism has two major concepts --> Overloading and Overriding.
#--------------------------------------------------------------------------------------------------------------------------
#overloading

class A:
    def one(self,check,*l):
        self.l = l
         
        ans = ""
        ans1 = 0
         
        if check == "str":
            for i in l:
                ans += i
            return ans
         
        elif check == "int":
            for i in l:
                ans1 += i
            return ans1
         
obj = A()
a = obj.one("str","one","two")
print(a)
b = obj.one("int",2,4)
print(b)

#--------------------------------------------
#overriding

class A:
    def one(self):
        print("A:one")
     
    def two(self):
        print("A:two")
         
class B(A):
    def one(self):
        print("B:one")
     
    def two(self):
        print("B:two")
 
obj1 = A()
obj1.one()
obj2 = B()
obj2.one()
