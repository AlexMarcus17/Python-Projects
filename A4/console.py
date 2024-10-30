from myvector import MyVector
from vectorrepo import VectorRepository
#prints the menu
def display_menu():
    print("1.Add vector to the repository.")
    print("2.Get all vectors.")
    print("3.Get a vector at a given index.")
    print("4.Update a vector at a given index.")
    print("5.Update a vector identified by name_id.")
    print("6.Delete a vector by index.")
    print("7.Delete a vector by name_id.")
    print("8.Plot all vectors.")
    print("9.Get the sum of all the elements")
    print("10.Delete all vectors.")
    print("11.Update the color of a vector identified by type.")
    print("12.Exit.")
#runs the app
def run_console():
    vector_repo = VectorRepository()
    vector_repo.add_vector(MyVector(1, "red", 3, [1, 4, 5]))
    vector_repo.add_vector(MyVector(2, "blue", 3, [2, 5, 6]))
    vector_repo.add_vector(MyVector(3, "green", 3, [3, 6, 7]))
    vector_repo.add_vector(MyVector(4, "yellow", 3, [4, 7, 8]))
    vector_repo.add_vector(MyVector(5, "red", 3, [5, 8, 9]))
    vector_repo.add_vector(MyVector(6, "blue", 3, [6, 9, 10]))
    vector_repo.add_vector(MyVector(7, "green", 3, [7, 10, 11]))
    vector_repo.add_vector(MyVector(8, "red", 3, [8, 11, 12]))
    vector_repo.add_vector(MyVector(9, "green", 3, [9, 12, 13]))
    vector_repo.add_vector(MyVector(10, "blue", 3, [10, 13, 14]))



    running = True
    while running:

        display_menu()
        num = input("Enter option:")
        if num == "1":
            name_id = input("Name Id: ")
            color = input("Color: ")
            type = int(input("Type: "))
            values_input = input("Enter the values separated by commas:")
            values = [int(val) for val in values_input.split(',')]
            new_vector = MyVector(name_id, color, type, values)
            vector_repo.add_vector(new_vector)

        elif num == "2":
            vector_repo.printvectors()

        elif num == "3":
            try:
                index = int(input("Enter the index:"))
                print(str(vector_repo.get_vector_index(index)))
            except:
                print("Invalid index")


        elif num == "4":
            try:
                index = int(input("Enter the index:"))
                name_id = input("Name Id: ")
                color = input("Color: ")
                type = int(input("Type: "))
                values_input = input("Enter the values separated by commas:")
                values = [int(val) for val in values_input.split(',')]
                new_vector = MyVector(name_id, color, type, values)
                vector_repo.update_vector_index(index, new_vector)
                vector_repo.printvectors()
            except ValueError:
                print("Invalid data!")

        elif num == "5":
            sname_id = int(input("Enter the name_id:"))
            name_id = input("Name Id: ")
            color = input("Color: ")
            type = int(input("Type: "))
            values_input = input("Enter the values separated by commas:")
            values = [int(val) for val in values_input.split(',')]
            new_vector = MyVector(name_id, color, type, values)
            vector_repo.update_vector_name(sname_id, new_vector)
            vector_repo.printvectors()

        elif num == "6":
            index = int(input("Enter the index: "))
            vector_repo.delete_vector_index(index)
            vector_repo.printvectors()

        elif num == "7":
            try:
                name_id = int(input("Enter the name_id: "))
                vector_repo.delete_vector_name(name_id)
                vector_repo.printvectors()
            except:
                print("Invalid name")
        elif num == "8":
            vector_repo.plot_vec()

        elif num == "9":
            print(vector_repo.get_sum_all())

        elif num == "10":
            vector_repo.delete_all()
            vector_repo.printvectors()

        elif num == "11":
            new_color = input("Enter new color:")
            type = int(input("Enter the type:"))
            vector_repo.update_color_by_type(type, new_color)
            vector_repo.printvectors()

        elif num == "12":
            running = False


