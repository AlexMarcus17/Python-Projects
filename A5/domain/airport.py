from domain.plane import Plane
from domain.passenger import Passenger
import unittest
class Airport:
    def __init__(self, planes):
        self.__planes = planes
    def getplanes(self):
        return self.__planes
    def setplanes(self, planes):
        self.__planes = planes
    def updateplane(self, index, plane):
        self.__planes[index] = plane
    def removeplane(self, index):
        del self.__planes[index]
    def getplane(self, index):
        return self.__planes[index]
    def sortbypassengers(self):
        self.__planes = sorted(self.__planes, key=lambda plane: len(plane.getpassengers()))

    def sortbyfirstnamestartswith(self, substring):

        self.__planes = sorted(self.__planes, key=lambda plane: sum(
            1 for passenger in plane.getpassengers() if passenger.getfname().startswith(substring)))

    def sortbyconcatenatedinfo(self):
        self.__planes = sorted(self.__planes,
                               key=lambda plane: f"{len(plane.getpassengers())}_{plane.getdestination()}")

    def identifyplanesbypassportnumber(self, passportprefix):
        matching_planes = [plane for plane in self.__planes if any(
            passenger.getnumber().startswith(passportprefix) for passenger in plane.getpassengers()
        )]
        return matching_planes

    def identifypassengers(self, plane, substring):
        passengers = self.__planes[plane].getpassengers()
        matching_passengers = [passenger for passenger in passengers if
                               substring in passenger.getfname() or substring in passenger.getlname()]
        return matching_passengers

    def identifyplanesbyperson(self, first_name, last_name):
        matching_planes = [plane for plane in self.__planes if any(
            person.getfname() == first_name and person.getlname() == last_name for person in plane.getpassengers()
        )]
        return matching_planes

    @staticmethod
    def backtracking_check(list, plane):

        for p in list:
            if plane.getdestination() != p.getdestination() or plane.getcompany() == p.getcompany():
                return False
        return True

    @staticmethod
    def backtracking(list, k, condition, current_sol=[], index=0):
        if k > len(list) or not isinstance(k, int):
            raise ValueError("Invalid k")
        if len(current_sol) == k:
            return [current_sol[:]]
        groups = []
        for i in range(index, len(list)):
            item = list[i]
            if not condition(current_sol, item):
                continue
            current_sol.append(item)
            l = Plane.backtracking(list, k, condition, current_sol, i + 1)
            groups.extend(l)
            current_sol.pop()
        return groups

    def printairport(self):
        for i in self.__planes:
            print(str(i))

class TestAirport(unittest.TestCase):
    def setUp(self):
        self.passenger1 = Passenger("P001", "John", "Sanders")
        self.passenger2 = Passenger("P002", "Jane", "Smith")
        self.passenger3 = Passenger("P003", "Bob", "Johnson")

        self.plane1 = Plane("PL001", "Airline1", 50, "Roma", [self.passenger1, self.passenger2])
        self.plane2 = Plane("PL002", "Airline2", 30, "Paris", [self.passenger3])

        self.airport = Airport([self.plane1, self.plane2])

    def test_get_planes(self):
        self.assertEqual(self.airport.getplanes(), [self.plane1, self.plane2])

    def test_set_planes(self):
        new_planes = [Plane("PL003", "Airline3", 40, "Madrid", [self.passenger1])]
        self.airport.setplanes(new_planes)
        self.assertEqual(self.airport.getplanes(), new_planes)

    def test_update_plane(self):
        new_plane = Plane("PL003", "Airline3", 40, "Madrid", [self.passenger1])
        self.airport.updateplane(0, new_plane)
        self.assertEqual(self.airport.getplanes(), [new_plane, self.plane2])

    def test_remove_plane(self):
        self.airport.removeplane(0)
        self.assertEqual(self.airport.getplanes(), [self.plane2])

    def test_get_plane(self):
        retrieved_plane = self.airport.getplane(1)
        self.assertEqual(retrieved_plane, self.plane2)

    def test_sort_by_firstname_startswith(self):
        # Ensure that the planes are sorted by the number of passengers whose first name starts with 'J'
        self.airport.sortbyfirstnamestartswith('J')
        self.assertEqual(self.airport.getplanes(), [ self.plane2,self.plane1])

    def test_sort_by_concatenated_info(self):
        # Ensure that the planes are sorted by the concatenated info (passenger count and destination)
        self.airport.sortbyconcatenatedinfo()
        self.assertEqual(self.airport.getplanes(), [self.plane2, self.plane1])

    def test_identify_planes_by_passport_number(self):
        matching_planes = self.airport.identifyplanesbypassportnumber('P00')
        self.assertEqual(matching_planes, [self.plane1, self.plane2])

    def test_identify_passengers(self):
        matching_passengers = self.airport.identifypassengers(0, 'Sanders')
        self.assertEqual(matching_passengers, [self.passenger1])

    def test_identify_planes_by_person(self):
        matching_planes = self.airport.identifyplanesbyperson('John', 'Sanders')
        self.assertEqual(matching_planes, [self.plane1])