class MyPoint:
    #constructor
    def __init__(self):
        self.__coord_x = 0.0
        self.__coord_y = 0.0
        self.__color = "blue"
    #getters and setters
    def getCoordX(self):
        return self.__coord_x
    def getCoordY(self):
        return self.__coord_y
    def getColor(self):
        return self.__color
    def setCoordX(self, coord_x):
        self.__coord_x = coord_x
    def setCoordY(self, coord_y):
        self.__coord_y = coord_y
    def setColor(self, color):
        self.__color = color
    #string converter function
    def __str__(self):
        return f"Point ({str(self.__coord_x)},{str(self.__coord_y)}) of color {self.__color}"