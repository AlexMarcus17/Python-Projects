import unittest
from vectorrepo import VectorRepository
from myvector import MyVector
class TestVectorRepositoryMethods(unittest.TestCase):

    def setUp(self):
        self.vector_repository = VectorRepository()
    def test_get_vectors(self):
        self.assertEqual(self.vector_repository.get_vectors(), [])

        vector1 = MyVector(1, 'red', 3, [1, 2, 3])
        vector2 = MyVector(2, 'blue', 3, [4, 5, 6])
        self.vector_repository.add_vector(vector1)
        self.vector_repository.add_vector(vector2)
        self.assertEqual(self.vector_repository.get_vectors(), [vector1, vector2])

        self.vector_repository.delete_all()
        self.assertEqual(self.vector_repository.get_vectors(), [])

    def test_add_vector(self):
        vector = MyVector(1, 'red', 3, [1, 2, 3])
        self.vector_repository.add_vector(vector)
        self.assertEqual(self.vector_repository.get_vectors(), [vector])

        vector2 = MyVector(2, 'blue', 3, [4, 5, 6])
        self.vector_repository.add_vector(vector2)
        self.assertEqual(self.vector_repository.get_vectors(), [vector, vector2])

        self.vector_repository.delete_all()
        self.assertEqual(self.vector_repository.get_vectors(), [])

    def test_get_vector_index(self):
        vector1 = MyVector(1, 'red', 3, [1, 2, 3])
        vector2 = MyVector(2, 'blue', 3, [4, 5, 6])
        self.vector_repository.add_vector(vector1)
        self.vector_repository.add_vector(vector2)

        self.assertEqual(self.vector_repository.get_vector_index(0), vector1)
        self.assertEqual(self.vector_repository.get_vector_index(1), vector2)

