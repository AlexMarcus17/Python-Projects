from pointrepo import PointRepository

#prints the menu
def print_menu():
    print("Please select an option")
    print("1.Add point to repository")
    print("2.Get all points")
    print("3.Get a point at a given index")
    print("4.Get all points of a given color")
    print("5.Get all points inside a given square(up-left corner and length)")
    print("6.Get the minimum distance between points")
    print("7.Update point at a given index")
    print("8.Delete point by index")
    print("9.Delete all points that are inside a given square")
    print("10.Plot all points")
    print("11.Get all points that are inside a given circle (center of circle, radius)")
    print("12.Update the color of a point given its coordinates")
    print("13.Delete a point by coordinates")
    print("14.Get all points inside a rectangle")
    print("15.Shift all points on x-axis")
    print("16.Delete all point inside a circle")
    print("17.Quit")


def print_point_repo(repo):
    point_list = []
    for point in repo:
        point_list.append(str(point))
    print(point_list)


def read_option():
    option = int(input("Option:"))
    while option not in [i for i in range(1, 18)]:
        print("Invalid option.")
        option = int(input("Please type in a valid option:"))
    return option


def get_input_1():
    [x, y] = input("Please type in the coordinates:").split()
    color = input("Please type in the color:")
    return float(x), float(y), color


def get_input_index():
    index = int(input("Please type in the index:"))
    return index


def get_input_color():
    color = input("Please type in the color:")
    return color


def get_input_square():
    [x, y, length] = input("Please type in the coordinates of the up-left corner and the length:").split()
    return float(x), float(y), float(length)

def get_input_rectangle():
    [x, y, length, width] = input("Please type in the coordinates of the up-left corner, the length and the width:").split()
    return float(x), float(y), float(length), float(width)

def get_x_shift():
    x = input("Enter the value: ")
    return x



def get_input_7():
    index = get_input_index()
    [x, y] = input("Please type in the new coordinates:").split()
    color = input("Please type in the new color:")
    return index, float(x), float(y), color


def get_input_circle():
    [x, y, radius] = input("Please type in the coordinates of the center and the radius:").split()
    return float(x), float(y), float(radius)


def get_input_coordinates():
    [x, y] = input("Please type in the coordinates:").split()
    return float(x), float(y)

#function that starts the app
def start_program():
    option = 0
    point_repo = PointRepository()
    while option != 17:
        print_menu()
        option = read_option()
        if option == 1:
            [x, y, color] = get_input_1()
            point_repo.add_point(x, y, color)
            print_point_repo(point_repo.get_all_points())
        if option == 2:
            all_points = point_repo.get_all_points()
            print_point_repo(all_points)
        if option == 3:
            index = get_input_index()
            wanted_point = point_repo.get_point_at_given_index(index)
            print(str(wanted_point))
        if option == 4:
            color = get_input_color()
            wanted_points = point_repo.get_points_of_given_color(color)
            print_point_repo(wanted_points)
        if option == 5:
            [x, y, length] = get_input_square()
            wanted_points = point_repo.get_points_inside_square(x, y, length)
            print_point_repo(wanted_points)
        if option == 6:
            min_distance = point_repo.get_minimum_distance_between_points()
            print(f"The minimum distance between all points is: {min_distance}")
        if option == 7:
            index, x, y, color = get_input_7()
            point_repo.update_point_at_given_index(index, x, y, color)
            print_point_repo(point_repo.get_all_points())
        if option == 8:
            index = get_input_index()
            point_repo.delete_point_by_index(index)
            print_point_repo(point_repo.get_all_points())
        if option == 9:
            [x, y, length] = get_input_square()
            point_repo.delete_points_inside_square(x, y, length)
            print_point_repo(point_repo.get_all_points())
        if option == 10:
            point_repo.plot_points()
        if option == 11:
            x, y, radius = get_input_circle()
            wanted_points = point_repo.get_points_inside_circle(x, y, radius)
            print_point_repo(wanted_points)
        if option == 12:
            x, y = get_input_coordinates()
            color = get_input_color()
            point_repo.update_color_by_coordinates(x, y, color)
            print_point_repo(point_repo.get_all_points())
        if option == 13:
            x, y = get_input_coordinates()
            point_repo.delete_by_coordinates(x, y)
            print_point_repo(point_repo.get_all_points())
        if option == 14:
            [x, y, length, width] = get_input_rectangle()
            lst = point_repo.get_points_inside_rectangle(x, y, length, width)
            print_point_repo(lst)
        if option == 15:
            x = get_x_shift()
            point_repo.shift_points_on_x(x)
            print_point_repo(point_repo.get_all_points())
        if option == 16:
            [x, y, radius] = get_input_circle()
            point_repo.delete_points_inside_a_circle(x, y, radius)
            print_point_repo(point_repo.get_all_points())
        if option == 17:
            break
