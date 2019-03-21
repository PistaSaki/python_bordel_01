class Parent:
    def __init__(self, x):
        self.x = x
        
    def __str__(self):
        return f"{type(self).__name__}({self.x})"
        
class Child(Parent):
    def __init__(self, y):
        x = y**2
        super().__init__(x)
        
c = Child(2)
print(c)
