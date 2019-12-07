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
    print("Calculating coordinates for wire path")
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
    print("Wire path calculated")
    print("Total wire path coordinates: "+str(len(coordinates)))
    return coordinates


def get_common_coordinates(coordinates_1, coordinates_2):
    print("Getting intersection coordinates for wire paths")
    print("Total possible combinations: "+str((len(coordinates_1)+1)*len(coordinates_2)+1))
    common = []
    i = 0
    y = 0
    for coord in coordinates_1:
        if coord in coordinates_2:
            y += 1
            common.append(coord)
        i += 1
    common.remove([0, 0])
    print("Found "+str(len(common))+" intersection coordinates")
    return common


def get_distances(common_points):
    print("Calculating manhattan distances for common points")
    distances = []
    for point in common_points:
        distances.append(distance.cityblock([0, 0], point))
    return distances


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


wire1_coordinates = get_coordinates(wire_1)
wire2_coordinates = get_coordinates(wire_2)

common_coordinates = get_common_coordinates(wire1_coordinates, wire2_coordinates)
manhattan_distances = get_distances(common_coordinates)
print("Part 1: " + str(min(manhattan_distances)))

intersection_common_distances = []

print("Calcuating route distance for both wires to reach each intersection")
for intersection in common_coordinates:
    wire1_route = wire1_coordinates.index(intersection)
    wire2_route = wire2_coordinates.index(intersection)
    intersection_common_distances.append(wire1_route+wire2_route)

print("Part 2: "+str(min(intersection_common_distances)))


