from domain.airport import Airport
from domain.passenger import Passenger
from domain.plane import Plane
def display_menu():
    print("1.Sort passengers in a plane by last name")
    print("2.Sort planes according to the number of passengers")
    print("3.Sort planes according to the number of passengers with the first name starting with a given substring")
    print("4.Sort planes according to the string obtained by concatenation of the number of passengers and destination")
    print("5.Identify  planes  that  have  passengers  with  passport  numbers  starting  with the same 3 letters")
    print("6.Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last name contain a string")
    print("7.Identify plane/planes where there is a passenger with given name")
    print("8.Form groups of 𝒌 passengers from the same plane but with different last names")
    print("9.Form groups of 𝒌 planes with  the  same  destination  but  belonging to  different airline companies")
    print("0.Exit")

def start():
    passenger1 = Passenger("1254", "Alex", "Marcus")
    passenger2 = Passenger("7547", "John", "Smith")
    passenger3 = Passenger("3653", "Mihai", "Pop")
    passenger4 = Passenger("7647", "Peter", "Johnson")
    passenger5 = Passenger("9584", "Max", "Ford")
    passenger6 = Passenger("7483", "Tom", "Williams")
    passenger7 = Passenger("9584", "Bruce", "Jones")
    passenger8 = Passenger("8673", "Brad", "Davies")
    passenger9 = Passenger("9592", "Scarlett", "Brown")
    passenger10 = Passenger("8592", "Jack", "Adams")

    plane1 = Plane(1, "WizAir", 50, "Bali",
                        [passenger1, passenger2, passenger3])
    plane2 = Plane(2, "RyanAir", 50, "Bucharest",
                        [passenger4, passenger5, passenger6, passenger7])
    plane3 = Plane(3, "TARom", 100, "Cyprus",
                        [passenger8, passenger9, passenger10])

    airport = Airport([plane1, plane2, plane3])
    airport.printairport()
    running = True
    while running:

        display_menu()
        num = input("Enter option:")
        if num == "1":
            try:
                plane_number = int(input("Please enter the index of the plane: "))
                plane = airport.getplanes()[plane_number]
                plane.sortpassengers()
            except:
                print("Invalid index")

        elif num == "2":
            airport.sortbypassengers()

        elif num == "3":
            substr1 = str(input("Please enter the substring: "))
            try:
                airport.sortbyfirstnamestartswith(substr1)
            except:
                print("Invalid substring")


        elif num == "4":
            airport.sortbyconcatenatedinfo()

        elif num == "5":
            try:
                substr1 = int(input("Please enter the prefix: "))
                lst = airport.identifyplanesbypassportnumber(substr1)
                for i in lst:
                    print(str(i))
            except:
                print("Invalid prefix")

        elif num == "6":
            try:
                index = int(input("Enter the plane index: "))
                str1 = str(input("Please enter the string: "))
                lst = airport.identifypassengers(index, str1)
                for i in lst:
                    print(str(i))
            except:
                print("Invalid index")


        elif num == "7":
            try:
                str2 = str(input("Please enter the first name: "))
                str3 = str(input("Please enter the last name: "))
                lst = airport.identifyplanesbyperson(str2,str3)
                for i in lst:
                    print(str(i))
            except:
                print("Invalid name")
        elif num == "8":
            try:
                plane_num = int(input("Please enter the index of the plane: "))
                k = int(input("Please enter k: "))
                groups = Plane.backtracking(airport.getplanes()[plane_num].getpassengers(), k, Plane.backtracking_check)
                for i in groups:
                    print("\n")
                    for j in i:
                        print(str(j))
            except:
                print("Invalid index")

        elif num == "9":
            try:
                k = int(input("Please enter k: "))
                groups = Airport.backtracking(airport.getplanes(), k , Airport.backtracking_check)
                for i in groups:
                    print("\n")
                    for j in i:
                        print(str(j))
            except:
                print("Invalid k")

        elif num == "0":
            running = False

        airport.printairport()
