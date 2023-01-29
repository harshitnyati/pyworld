class Parent():
      
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"
        print(self.value)
          
    # Parent's show method
    def show(self):
        print(self.value)
          
# Defining child class
class Child(Parent):
      
    # Constructor
    def __init__(self):
        self.value = "Inside Child"
        print(self.value)
          
    # Child's show method
    def show(self):
        print("show of child")
        print(self.value)
          
          
# Driver's code
# obj1 = Parent()
obj2 = Child()
  
# obj1.show()
obj2.show()