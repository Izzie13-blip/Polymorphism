class Hexagon:

    def __init__(self):
        self.__sides= 6


    def side(self):
        print("Sides:{}".format(self.__sides))

    def setSides(self, sides):
        self.__sides = sides

h=Hexagon()
h.side()

#change the sides
h.__sides=10
h.side()

#using setter function
h.setSides(10)
h.side()