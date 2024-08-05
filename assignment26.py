#Point
class Point:    # capitalize the first letter after the point (pascag),point is the object
    def __init__(self, x, y): #this message s a constructor,it is used to construct or create an object
        self.x = x  #self.x is the attribute and x is th argument
        self.y = y

    def move(self): #functions
        print("move")
    def draw(self):
        print("draw")


point = Point(10,20)    # braket very important   # this is object they define a class
# point1.x = 10     # attributes
# point1.y = 20
print(point.x)
point.draw()
