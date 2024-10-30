import math
import matplotlib.pyplot as plt
from point import *


class PointRepository:
    #the constructor adds 10 data examples to the point list
    def __init__(self):
        p1 = MyPoint()
        p1.setCoordX(1)
        p1.setCoordY(2)
        p1.setColor("blue")
        p2 = MyPoint()
        p2.setCoordX(3)
        p2.setCoordY(4)
        p2.setColor("red")
        p3 = MyPoint()
        p3.setCoordX(5)
        p3.setCoordY(6)
        p3.setColor("green")
        p4 = MyPoint()
        p4.setCoordX(4)
        p4.setCoordY(3)
        p4.setColor("blue")
        p5 = MyPoint()
        p5.setCoordX(2)
        p5.setCoordY(2)
        p5.setColor("yellow")
        p6 = MyPoint()
        p6.setCoordX(3)
        p6.setCoordY(2)
        p6.setColor("blue")
        p7 = MyPoint()
        p7.setCoordX(1)
        p7.setCoordY(6)
        p7.setColor("red")
        p8 = MyPoint()
        p8.setCoordX(4)
        p8.setCoordY(7)
        p8.setColor("green")
        p9 = MyPoint()
        p9.setCoordX(2)
        p9.setCoordY(3)
        p9.setColor("red")
        p10 = MyPoint()
        p10.setCoordX(7)
        p10.setCoordY(3)
        p10.setColor("magenta")
        self.__repository = [
            p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
        ]
    #adds a point to the list
    def add_point(self, x, y, color):
        point = MyPoint()
        point.setCoordX(x)
        point.setCoordY(y)
        point.setColor(color)
        self.__repository.append(point)
    #point list getter
    def get_all_points(self):
        return self.__repository
    #returns a point at a given index
    def get_point_at_given_index(self, index):
        try:
            return self.__repository[index]
        except IndexError:
            print("Invalid Index")
    #returns points of a given color
    def get_points_of_given_color(self, color):
        if color not in ["red", "green", "blue", "magenta", "yellow"]:
            raise ValueError("Invalid color")
        else:
            points_list = []
            for point in self.__repository:
                if point.getColor() == color:
                    points_list.append(point)
            return points_list
    #updates a point at a given index
    def update_point_at_given_index(self, index, x, y, color):
        try:
            point = self.get_point_at_given_index(index)

        except IndexError:
            print("Invalid index.")
        try:
            point.setCoordX(x)
            point.setCoordY(y)
            point.setColor(color)
        except ValueError:
            print("Invalid data")
    #updates a color by point coordinates
    def update_color_by_coordinates(self, x, y, color):
        found = 0
        for point in self.__repository:
            if point.getCoordX() == float(x) and point.getCoordY() == float(y):
                point.setColor(color)
                found = 1
        if found == 0:
            print("Point not found.")
    #deletes a point by index
    def delete_point_by_index(self, index):
        try:
            self.__repository.pop(index)
        except IndexError:
            print("Invalid index.")

    # deletes a point by coordinates
    def delete_by_coordinates(self, x, y):
        found = 0
        for point in self.__repository:
            if point.getCoordX() == float(x) and point.getCoordY() == float(y):
                found = 1
                self.__repository.remove(point)
        if found == 0:
            print("Point not found.")
    #plot all points
    def plot_points(self):
        x = [point.getCoordX() for point in self.__repository]
        y = [point.getCoordY() for point in self.__repository]
        col = [point.getColor() for point in self.__repository]

        plt.scatter(x, y, c=col)
        plt.show()
    #gets all the points inside a given circle
    def get_points_inside_circle(self, x_center, y_center, radius):
        point_list = []
        for point in self.__repository:
            if (x_center - point.getCoordX()) ** 2 + (y_center - point.getCoordY()) ** 2 <= radius ** 2:
                point_list.append(point)
        return point_list
    #returns the minimum distance between the points
    def get_minimum_distance_between_points(self):
        minimum_distance = 9999999999999999
        for index1 in range(len(self.__repository) - 1):
            for index2 in range(index1 + 1, len(self.__repository)):
                x1 = self.__repository[index1].getCoordX()
                x2 = self.__repository[index2].getCoordX()
                y1 = self.__repository[index1].getCoordY()
                y2 = self.__repository[index2].getCoordY()

                distance = math.sqrt((x2 - x1)**2 + (y2 - y1) ** 2)
                if distance < minimum_distance:
                    minimum_distance = distance
        return minimum_distance
    #returns all points inside a given square
    def get_points_inside_square(self, x, y, length):
        inside_points = []
        for point in self.__repository:
            point_x = point.getCoordX()
            point_y = point.getCoordY()
            if x <= point_x <= x + length and y - length <= point_y <= y:
                inside_points.append(point)
        return inside_points

    # returns all points inside a given rectangle
    def get_points_inside_rectangle(self, x, y, length, width):
        inside_points = []
        for point in self.__repository:
            point_x = point.getCoordX()
            point_y = point.getCoordY()
            if x <= point_x <= x + length and y <= point_y <= y + width:
                inside_points.append(point)
        return inside_points
    #number of points of a given color
    def get_points_by_color(self, color):
        num = 0
        for i in self.__repository:
            if(i.getColor()==color):
                num+=1
        return num
    #updates a color by coordinates
    def update_color_by_coord(self, x, y, newcolor):
        for i in self.__repository:
            if(i.getCoordX==x and i.getCoordY==y):
                i.setColor(newcolor)
    #shifts points on y-axis
    def shift_points_on_y(self, value):
        for i in range(len(self.__repository)):
            self.__repository[i].setCoordY(self.__repository[i].getCoordY()+value)
    #deletes all points inside a square
    def delete_points_inside_square(self, x, y, length):
        points_to_delete = self.get_points_inside_square(x, y, length)
        for point in points_to_delete:
            self.__repository.remove(point)
    #returns the maximum distance
    def get_maximum_distance(self):
        maximum_distance = -1.0
        for index1 in range(len(self.__repository) - 1):
            for index2 in range(index1 + 1, len(self.__repository)):
                x1 = self.__repository[index1].getCoordX()
                x2 = self.__repository[index2].getCoordX()
                y1 = self.__repository[index1].getCoordY()
                y2 = self.__repository[index2].getCoordY()

                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if distance > maximum_distance:
                    maximum_distance = distance
        return maximum_distance
    #shifts all points on x-axis
    def shift_points_on_x(self, value):
        for i in range(len(self.__repository)):
            self.__repository[i].setCoordX(self.__repository[i].getCoordX()+int(value))
    #deletes all points whithin a distance by a point
    def delete_all_points_within_a_distance(self, distance, point):
        for i in range(len(self.__repository)):
            x1 = self.__repository[i].getCoordX()
            x2 = point.getCoordX()
            y1 = self.__repository[i].getCoordY()
            y2 = point.getCoordY()
            distance2 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if(distance2<distance):
                self.__repository.remove(i)
    #deletes all points inside a given circle
    def delete_points_inside_a_circle(self, x_center, y_center, radius):
        for point in self.__repository:
            if (x_center - point.getCoordX()) ** 2 + (y_center - point.getCoordY()) ** 2 <= radius ** 2:
                self.delete_by_coordinates(point.getCoordX(),point.getCoordY())



