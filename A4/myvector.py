import numpy as np

class MyVector:
    def __init__(self, name_id, colour, type, values):
        self.__name_id = name_id
        self.__colour = colour
        self.__type = type
        self.__values = values
    #overrides the string function
    def __str__(self):
        str1 = "Vector "
        str1 += str(self.__name_id)
        str1 += ", color "
        str1 += self.__colour
        str1 += ", ["
        for i in self.__values:
            str1 += str(i)
            str1 += ","
        str1 += "]"
        return str1

    #getters
    def get_name_id(self):
        return self.__name_id
    def get_colour(self):
        return self.__colour
    def get_type(self):
        return self.__type
    def get_values(self):
        return self.__values
    #prints the values inside the array
    def print_values(self):
        str1 = "["
        for i in self.__values:
            str1+= str(i)
            str1+= ","
        str1 += "]"
        print(str1)

    #setters
    def set_name_id(self, name_id):
        self.__name_id = name_id
    def set_colour(self, colour):
        self.__colour = colour
    def set_type(self, type):
        self.__type = type
    def set_values(self, values):
        self.__values = values

    #performs vector operations
    def add_scalar(self, scalar):
        for i in range(len(self.__values)):
            self.__values[i] = self.__values[i] + scalar
    def add_vector(self, vector):
        lst = vector.get_values()
        for i in range(len(self.__values)):
            self.__values[i] = self.__values[i] + lst[i]
    def substract_vector(self, vector):
        lst = vector.get_values()
        for i in range(len(self.__values)):
            self.__values[i] = self.__values[i] - lst[i]
    def multiply_vectors(self, vector):
        num = 0
        lst = vector.get_values()
        for i in range(len(self.__values)):
            num += (lst[i]*self.__values[i])
        return num
    def sum(self):
        num = 0
        for i in range(len(self.__values)):
            num+=self.__values[i]
        return num
    def product(self):
        num = 1
        for i in range(len(self.__values)):
            num *= self.__values[i]
        return num
    def average(self):
        num = 0
        for i in range(len(self.__values)):
            num += self.__values[i]
        return num/len(self.__values)
    def minimum(self):
        min = self.__values[0]
        for i in range(len(self.__values)):
            if(min>self.__values[i]):
                min = self.__values[i]
        return min
    def maximum(self):
        max = self.__values[0]
        for i in range(len(self.__values)):
            if(max<self.__values[i]):
                max = self.__values[i]
        return max

    #performs vector operations using numpy library

    def add_scalar2(self, scalar):
        numpy_values = np.array(self.get_values())
        numpy_values += scalar
        self.set_values(numpy_values.tolist())

    def add_vector2(self, vector2):
        numpy_vector_1 = np.array(self.get_values())
        numpy_vector_2 = np.array(vector2)
        result = numpy_vector_1 + numpy_vector_2
        self.set_values(result.tolist())

    def subtract_vector2(self, vector2):
        numpy_vector_1 = np.array(self.get_values())
        numpy_vector_2 = np.array(vector2)
        result = numpy_vector_1 - numpy_vector_2
        self.set_values(result.tolist())

    def sum2(self):
        numpy_array = np.array(self.get_values())
        return numpy_array.sum()

    def product2(self):
        numpy_array = np.array(self.get_values())
        return numpy_array.prod()

    def average2(self):
        numpy_array = np.array(self.get_values())
        return numpy_array.sum() / numpy_array.size

    def min2(self):
        numpy_array = np.array(self.get_values())
        return np.min(numpy_array)

    def max2(self):
        numpy_array = np.array(self.get_values())
        return np.max(numpy_array)



