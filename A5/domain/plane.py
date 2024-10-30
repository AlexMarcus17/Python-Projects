import unittest
from domain.passenger import Passenger
class Plane:
    def __init__(self, number, company, seats, destination, passengers):
        self.__number = number
        self.__company = company
        self.__seats = seats
        self.__destination = destination
        self.__passengers = passengers
    def setnumber(self, newnum):
        try:
            self.__number = newnum
        except:
            print("Invalid number")
    def setcompany(self, company):
        self.__company = company
    def setseats(self, seats):
        if(seats<1):
            print("Invalid number")
        else:
            try:
                self.__seats = seats
            except:
                print("Invalid number")
    def setdestination(self, dest):
        self.__destination = dest
    def setpassengers(self, passengers):
        self.__passengers = passengers
    def addpassenger(self, passenger):
        self.__passengers.append(passenger)
    def deletepassengers(self):
        self.__passengers = []
    def getnumber(self):
        return self.__number
    def getcompany(self):
        return self.__company
    def getseats(self):
        return self.__seats
    def getdestination(self):
        return self.__destination
    def getpassengers(self):
        return self.__passengers
    def deletepassenger(self, index):
        try:
            del self.__passengers[index]
        except:
            print("Invalid index")
    def updatepassenger(self, index, passenger):
        try:
            self.__passengers[index] = passenger
        except:
            print("Invalid index")
    def getpassenger(self, index):
        try:
            return self.__passengers[index]
        except:
            print("Invalid index")

    def sortpassengers(self):
        self.__passengers = sorted(self.__passengers, key=lambda passenger: passenger.getlname())



    @staticmethod
    def backtracking_check(list, passenger):

        for p in list:
            if p.getlname() == passenger.getlname():
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
            l = Plane.backtracking(list, k, condition, current_sol, i+1)
            groups.extend(l)
            current_sol.pop()
        return groups
    def __str__(self):
        passengers = "\nPassengers: "
        for i in self.__passengers:
            passengers += "\n" + str(i)
        return ("Plane " + str(self.getnumber()) + f" Airline: {self.getcompany()}" +
                f" Destination: {self.getdestination()}" + f" with capacity: {self.getseats()}" +
                passengers
                )




class TestPlane(unittest.TestCase):

    def setUp(self):
        passengers = []
        passengers.append(Passenger(1,"John", "Smith"))
        passengers.append(Passenger(2,"Will", "Jackson"))
        passengers.append(Passenger(3, "Andrew", "Johnson"))
        self.plane = Plane(1, "Wizzair", 20, "Roma", passengers)

    def testnumber(self):
        self.assertEqual(self.plane.getnumber(), 1)
        self.plane.setnumber(2)
        self.assertEqual(self.plane.getnumber(), 2)

    def testcompany(self):
        self.assertEqual(self.plane.getcompany(), "Wizzair")
        self.plane.setcompany("Lufthansa")
        self.assertEqual(self.plane.getcompany(), "Lufthansa")
    def testseats(self):
        self.plane.setseats(-10)
        self.assertEqual(self.plane.getseats(), 20)
        self.plane.setseats(10)
        self.assertEqual(self.plane.getseats(), 10)
    def testdestination(self):
        self.assertEqual(self.plane.getdestination(), "Roma")
        self.plane.setdestination("Paris")
        self.assertEqual(self.plane.getdestination(), "Paris")

    def testpassengers(self):
        passenger = Passenger(4,"John", "Sanders")
        self.plane.updatepassenger(-2, passenger)
        self.plane.updatepassenger(2, passenger)
        self.assertEqual(self.plane.getpassenger(2), passenger)
        self.plane.deletepassenger(0)
        self.plane.deletepassenger(0)
        self.plane.deletepassenger(0)
        self.plane.deletepassenger(0)
        self.assertEqual(self.plane.getpassengers(), [])


