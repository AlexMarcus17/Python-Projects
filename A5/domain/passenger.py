import unittest
class Passenger:
    def __init__(self, pnumber, fname, lname):
        self.__pnumber = pnumber
        self.__fname = fname
        self.__lname = lname
    def setnumber(self, newnum):
        self.__pnumber = newnum
    def setfname(self, newname):
        self.__fname = newname
    def setlname(self, newname):
        self.__lname = newname
    def getnumber(self):
        return self.__pnumber
    def getfname(self):
        return self.__fname
    def getlname(self):
        return self.__lname
    def __str__(self):


        return self.getfname() + " " + self.getlname() + ", PassportID:" + self.getnumber()

class TestPassenger(unittest.TestCase):
    def setUp(self):
        self.passenger1 = Passenger(1, "John","Smith")
        self.passenger2 = Passenger(2, "Will", "Morris")
        self.passenger3 = Passenger(3, "Andrew", "Jackson")

    def testlname(self):
        self.assertEqual(self.passenger1.getlname(), "Smith")
        self.passenger1.setlname("Sanders")
        self.assertEqual(self.passenger1.getlname(), "Sanders")

    def testfname(self):
        self.assertEqual(self.passenger2.getfname(), "Will")
        self.passenger2.setfname("Jack")
        self.assertEqual(self.passenger2.getfname(), "Jack")

    def testnumber(self):
        self.assertEqual(self.passenger3.getnumber(), 3)
        self.passenger3.setnumber(4)
        self.assertEqual(self.passenger3.getnumber(), 4)
