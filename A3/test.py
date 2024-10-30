import unittest
from point import MyPoint
from pointrepo import PointRepository

class TestPointRepository(unittest.TestCase):

    def setUp(self):
        # Initialize a PointRepository for testing
        self.repository = PointRepository()

    def test_add_point(self):
        self.repository.add_point(10, 20, "orange")
        self.assertEqual(len(self.repository.get_all_points()), 11)

    def test_get_all_points(self):
        points = self.repository.get_all_points()
        self.assertIsInstance(points, list)
        for point in points:
            self.assertIsInstance(point, MyPoint)

    def test_get_point_at_given_index(self):
        point = self.repository.get_point_at_given_index(0)
        self.assertIsInstance(point, MyPoint)

    def test_get_points_of_given_color(self):
        red_points = self.repository.get_points_of_given_color("red")
        for point in red_points:
            self.assertEqual(point.getColor(), "red")

    def test_update_point_at_given_index(self):
        self.repository.update_point_at_given_index(0, 5, 5, "purple")
        updated_point = self.repository.get_point_at_given_index(0)
        self.assertEqual(updated_point.getCoordX(), 5)
        self.assertEqual(updated_point.getCoordY(), 5)
        self.assertEqual(updated_point.getColor(), "purple")

    def test_update_color_by_coordinates(self):
        self.repository.update_color_by_coordinates(1, 2, "purple")
        updated_point = self.repository.get_point_at_given_index(0)
        self.assertEqual(updated_point.getColor(), "purple")

    def test_delete_point_by_index(self):
        initial_length = len(self.repository.get_all_points())
        self.repository.delete_point_by_index(0)
        self.assertEqual(len(self.repository.get_all_points()), initial_length - 1)

    def test_delete_by_coordinates(self):
        initial_length = len(self.repository.get_all_points())
        self.repository.delete_by_coordinates(1, 2)
        self.assertEqual(len(self.repository.get_all_points()), initial_length - 1)

    def test_plot_points(self):
        # This is a visual test and needs to be checked manually
        self.repository.plot_points()

    def test_get_points_inside_circle(self):
        circle_points = self.repository.get_points_inside_circle(0, 0, 5)
        for point in circle_points:
            distance = (point.getCoordX()) ** 2 + (point.getCoordY()) ** 2
            self.assertTrue(distance <= 25)