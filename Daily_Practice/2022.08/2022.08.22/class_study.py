class Point:
    # Point class represents and manipulates x, y coordinates 
    def __init__(self, x = 0, y = 0):
    # create a new point at origin
        self.x = x
        self.y = y

    def distance(self):
        return ((self.x ** 2) + (self.y ** 2) ** 0.5)
    
    def to_string(self):
        print("{0}, {1}".format(self.x, self.y))

