class Coordinate(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance(self, other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    
    
c=Coordinate(3,4)
origin=Coordinate(0,0) 

class Person:
    name='Liu shimin'
    age='33'
    def greet(self):
        print('Hi, my name is '+self.name)
        
        
p1 = Person()

p1.greet()        
        