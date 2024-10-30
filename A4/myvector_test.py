import unittest
from myvector import MyVector
class TestMyVectorMethods(unittest.TestCase):
    def test_get_name_id(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.assertEqual(my_vector.get_name_id(), 1)
        my_vector.set_name_id(42)
        self.assertEqual(my_vector.get_name_id(), 42)
        my_vector.add_scalar(5)
        self.assertEqual(my_vector.get_name_id(), 42)

    def test_get_colour(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.assertEqual(my_vector.get_colour(), 'red')
        my_vector.set_colour('blue')
        self.assertEqual(my_vector.get_colour(), 'blue')
        my_vector.add_scalar(5)
        self.assertEqual(my_vector.get_colour(), 'blue')

    def test_get_type(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.assertEqual(my_vector.get_type(), 3)
        my_vector.add_scalar(5)
        self.assertEqual(my_vector.get_type(), 3)

    def test_get_values(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.assertEqual(my_vector.get_values(), [1, 2, 3])
        my_vector.set_values([4, 5, 6])
        self.assertEqual(my_vector.get_values(), [4, 5, 6])
        my_vector.add_scalar(5)
        self.assertEqual(my_vector.get_values(), [9, 10, 11])


    def test_set_name_id(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        my_vector.set_name_id(42)
        self.assertEqual(my_vector.get_name_id(), 42)
        my_vector.set_name_id(10)
        self.assertEqual(my_vector.get_name_id(), 10)
        my_vector.add_scalar(5)
        self.assertEqual(my_vector.get_name_id(), 10)

    def test_set_colour(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        my_vector.set_colour('blue')
        self.assertEqual(my_vector.get_colour(), 'blue')
        my_vector.set_colour('green')
        self.assertEqual(my_vector.get_colour(), 'green')
        my_vector.add_scalar(5)
        self.assertEqual(my_vector.get_colour(), 'green')


    def test_add_scalar(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        my_vector.add_scalar(5)
        self.assertEqual(my_vector.get_values(), [6, 7, 8])
        my_vector.add_scalar(-3)
        self.assertEqual(my_vector.get_values(), [3, 4, 5])
        my_vector.add_scalar(0)
        self.assertEqual(my_vector.get_values(), [3, 4, 5])

    def test_add_vector(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        other_vector = MyVector(1, 'red', 3, [4, 5, 6])
        my_vector.add_vector(other_vector)
        self.assertEqual(my_vector.get_values(), [5, 7, 9])
        other_vector.set_values([2, 3, 1])
        my_vector.add_vector(other_vector)
        self.assertEqual(my_vector.get_values(), [7, 10, 10])
        my_vector.add_vector(MyVector(1, 'red', 3, [0, 0, 0]))
        self.assertEqual(my_vector.get_values(), [7, 10, 10])

    def test_subtract_vector(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        other_vector = MyVector(1, 'red', 3, [4, 5, 6])
        my_vector.substract_vector(other_vector)
        self.assertEqual(my_vector.get_values(), [-3, -3, -3])
        other_vector.set_values([2, 3, 1])
        my_vector.substract_vector(other_vector)
        self.assertEqual(my_vector.get_values(), [-5, -6, -4])
        my_vector.substract_vector(MyVector(1, 'red', 3, [0, 0, 0]))
        self.assertEqual(my_vector.get_values(), [-5, -6, -4])

    def test_multiply_vectors(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        other_vector = MyVector(1, 'red', 3, [4, 5, 6])
        result = my_vector.multiply_vectors(other_vector)
        self.assertEqual(result, 32)
        other_vector.set_values([2, 3, 1])
        result = my_vector.multiply_vectors(other_vector)
        self.assertEqual(result, 11)
        result = my_vector.multiply_vectors(MyVector(1, 'red', 3, [0, 0, 0]))
        self.assertEqual(result, 0)

    def test_sum(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.assertEqual(my_vector.sum(), 6)
        my_vector.set_values([4, -2, 8])
        self.assertEqual(my_vector.sum(), 10)
        my_vector.add_scalar(0)
        self.assertEqual(my_vector.sum(), 10)

    def test_product(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.assertEqual(my_vector.product(), 6)
        my_vector.set_values([4, -2, 8])
        self.assertEqual(my_vector.product(), -64)
        my_vector.add_scalar(1)
        self.assertEqual(my_vector.product(), -45)

    def test_average(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.assertEqual(my_vector.average(), 2)
        my_vector.set_values([4, -2, 8])
        self.assertEqual(my_vector.average(), 10 / 3)
        my_vector.add_scalar(0)
        self.assertEqual(my_vector.average(), 10 / 3)

    def test_minimum(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.assertEqual(my_vector.minimum(), 1)
        my_vector.set_values([4, -2, 8])
        self.assertEqual(my_vector.minimum(), -2)
        my_vector.add_scalar(0)
        self.assertEqual(my_vector.minimum(), -2)

    def test_maximum(self):
        my_vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.assertEqual(my_vector.maximum(), 3)
        my_vector.set_values([4, -2, 8])
        self.assertEqual(my_vector.maximum(), 8)
        my_vector.add_scalar(0)
        self.assertEqual(my_vector.maximum(), 8)