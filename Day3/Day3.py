import json
import sys
from scipy.spatial import distance
import matplotlib.pyplot as plt

with open("input.json") as file:
    data = json.load(file)
file.close()

wire_1 = data["Wire1"].split(',')
wire_2 = data["Wire2"].split(',')


def get_coordinates(path_data):
    coordinates = [[0, 0]]
    for instruction in path_data:

        direction = instruction[0]
        dist = int(instruction[1:])

        if direction == 'R':
            for x in range(dist):
                current_coordinate = coordinates[len(coordinates) - 1]
                coordinates.append([current_coordinate[0] + 1, current_coordinate[1]])
        if direction == 'L':
            for x in range(dist):
                current_coordinate = coordinates[len(coordinates) - 1]
                coordinates.append([current_coordinate[0] - 1, current_coordinate[1]])
        if direction == 'U':
            for x in range(dist):
                current_coordinate = coordinates[len(coordinates) - 1]
                coordinates.append([current_coordinate[0], current_coordinate[1] + 1])
        if direction == 'D':
            for x in range(dist):
                current_coordinate = coordinates[len(coordinates) - 1]
                coordinates.append([current_coordinate[0], current_coordinate[1] - 1])
    return coordinates


def get_common_coordinates(coordinates_1, coordinates_2):
    common = []
    i = 0
    y = 0
    for coord in coordinates_1:
        sys.stdout.write("Checking coordinate no " + str(i) + " Common coordinates found: " + str(y) + "\r")
        sys.stdout.flush()
        if coord in coordinates_2:
            y += 1
            common.append(coord)
        i += 1
    common.remove([0, 0])
    return common


def get_distances(common_points):
    distances = []
    for point in common_points:
        distances.append(distance.cityblock([0, 0], point))
    return distances


wire1_coordinates = get_coordinates(wire_1)
wire2_coordinates = get_coordinates(wire_2)


# manhattan_distances = get_distances(get_common_coordinates(wire1_coordinates, wire2_coordinates))
# print(min(manhattan_distances))


def plot_wires(wire1, wire2):
    x_axis_wire1 = []
    y_axis_wire1 = []

    x_axis_wire2 = []
    y_axis_wire2 = []

    for coord in wire1:
        x_axis_wire1.append(coord[0])
        y_axis_wire1.append(coord[1])
    for coord in wire2:
        x_axis_wire2.append(coord[0])
        y_axis_wire2.append(coord[1])

    plt.title("Wire Map", fontsize=18)
    wire1 = plt.scatter(x_axis_wire1, y_axis_wire1, s=1, c="red")
    wire2 = plt.scatter(x_axis_wire2, y_axis_wire2, s=1, c="blue")
    plt.legend((wire1, wire2), ("Wire 1", "Wire 2"))
    plt.savefig("plot.png")


plot_wires(wire1_coordinates, wire2_coordinates)
