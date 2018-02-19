# Create a SquareGeometry class which takes in length as initialize parameter.
#  Make two methods g:etArea and getPerimeter inside this class.
# Which when invoked returns area and perimeter of each square instance.

class SquareGeometry:
    def __init__(self,length):
        self.length=length

    def getArea(self):
        return self.length**2

    def getPerimeter(self):
        return self.length*4

values= SquareGeometry(2)
print(values.getArea())
print(values.getPerimeter())
