
#Create a class Circle which has a class variable PI with value=22/7.
#Make two methods getArea and getCircumference inside this Circle class.
#Which when invoked returns area and circumference of each circle instances.


class Circle:
    PI=22/7
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        return Circle.PI*self.radius**2
    def getCircumference(self):
        return Circle.PI*self.radius*2


rad=Circle(5)
print(rad.getArea())
print(rad.getCircumference())
