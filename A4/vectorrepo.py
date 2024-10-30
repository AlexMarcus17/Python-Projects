import matplotlib.pyplot as plt
from myvector import MyVector
import unittest

class VectorRepository:
    def __init__(self):
        self.__vectors = []
    #gets all the vectors
    def get_vectors(self):
        return self.__vectors
    #prints all the vectors
    def printvectors(self):
        for i in self.__vectors:
            print(i)
    #adds a vector to the repo
    def add_vector(self, vector):
        color = vector.get_colour()
        if not(color=="red" or color=="blue" or color=="yellow" or color=="green" or color=="magenta"):
            print("Invalid color")
        else:
            self.__vectors.append(vector)
    #get vector by index
    def get_vector_index(self, index):
        try:
            return self.__vectors[index]
        except:
            print("Invalid index")

    #updates vector by index
    def update_vector_index(self, index, vector):
        color = vector.get_colour()
        if not (color == "red" or color == "blue" or color == "yellow" or color == "green" or color == "magenta"):
            print("Invalid color")
        else:
            try:
                self.__vectors[index] = vector
            except:
                print("Invalid index")
    #updates vector by name
    def update_vector_name(self, name, vector):
        color = vector.get_colour()
        if not (color == "red" or color == "blue" or color == "yellow" or color == "green" or color == "magenta"):
            print("Invalid color")
        else:
            try:
                for v in range(0,len(self.__vectors)):
                    if self.__vectors[v].get_name_id() == name:
                        self.__vectors[v] = vector
            except:
                print("Invalid name")

    #deletes vector by index
    def delete_vector_index(self, index):
        try:
            del self.__vectors[index]
        except:
            print("Invalid index")
    #deletes vector by name
    def delete_vector_name(self, name):
        try:
            for v in range(0,len(self.__vectors)):
                if self.__vectors[v].get_name_id() == name:
                    del self.__vectors[v]
        except:
            print("Invalid name")

    #returns the sum of all the values
    def get_sum_all(self):
        sum = 0
        for i in self.__vectors:
            sum += i.sum()
        return sum
    #deletes the vectors from the repo
    def delete_all(self):
        self.__vectors = []

    #updates the color by type
    def update_color_by_type(self, type, color):
        if not(color=="red" or color=="blue" or color=="yellow" or color=="green" or color=="magenta"):
            print("Invalid color")
        else:
            try:
                for i in range(0, len(self.__vectors)):
                    if self.__vectors[i].get_type() == type:
                        self.__vectors[i].set_colour(color)
            except:
                print("Invalid type")
    #plots all the vectors
    def plot_vec(self):
        plt.grid()
        all_vectors = self.__vectors
        type_dict = {
            1: "o",
            2: "s",
            3: "^",
            4: "D",
        }

        for i in range(len(all_vectors)):
            vector_type = all_vectors[i].get_type()
            if vector_type not in type_dict.keys():
                vector_type = "D"
            else:
                vector_type = type_dict[vector_type]
            plt.plot([i for i in range(len(all_vectors[i].get_values()))], all_vectors[i].get_values(),
                     marker=vector_type, c=all_vectors[i].get_colour())
        plt.show()