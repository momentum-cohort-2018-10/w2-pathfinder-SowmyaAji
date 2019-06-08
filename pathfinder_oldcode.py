from PIL import Image, ImageColor
import sys
import random

# pathfinder program old code
with open("elevation_small.txt") as text_file:
    # for lines in text_file:
    elevation_data = []
    for line in text_file.readlines():
        elevation_data.append([int(every_number)
                               for every_number in line.strip().split()])

# print(elevation_data)


def find_max_elevation(data):
    current_max = None
    for line in data:
        line_max = max(line)
        if current_max is None or line_max > current_max:
            current_max = line_max
    return current_max


max_elevation = find_max_elevation(elevation_data)
# print("maximum elevation is:", max_elevation)


def find_min_elevation(data):
    current_min = None
    for line in data:
        line_min = min(line)
        if current_min is None or line_min < current_min:
            current_min = line_min
    return current_min


min_elevation = find_min_elevation(elevation_data)

map_image = Image.new('RGBA', [len(elevation_data[0]), len(elevation_data)])

for row in range(len(elevation_data)):
    for column in range(len(elevation_data[0])):
        figure = elevation_data[row][column]
        bright = int(((figure - min_elevation) /
                      (max_elevation - min_elevation)) * 255)
        map_image.putpixel((column, row), (bright, bright, bright))
# map_image.save("elevation_map.png")


def find_path(elevation_data):
    # get the start_point

    #  1.5) draw the pixel at the current location
    #   2) Get the elevations for [row-1][current_column + 1], [row][current_column + 1], [row][current_column + 1]
    #  3) Find the difference between current_elevation and other elevations computed in step 2
    #  4) Find the smallest of the three differences
    #  5) Follow the path of the smallest difference by setting the current_row to be either row -1, row , row+1 depending on what you find in 4
    #
    current_row = 300
    current_column = 0

    while current_column < len(elevation_data[0]) and current_column >= 0:

        elevation = elevation_data[current_row][current_column]
        map_image.putpixel((current_column, current_row), (0, 255, 255))
        if current_column + 1 < len(elevation_data[0]):
            elevations = [sys.maxsize, sys.maxsize, sys.maxsize]
            if current_row > 0:
                elevations[0] = elevation_data[current_row -
                                               1][current_column + 1]
            elevations[1] = elevation_data[current_row][current_column + 1]
            if current_row + 1 < len(elevation_data):
                elevations[2] = elevation_data[current_row +
                                               1][current_column + 1]

            differences = [abs(elevation - next_elevation)
                           for next_elevation in elevations]
            smallest_diff_index = differences.index(min(differences))

            if smallest_diff_index == 0:
                current_row = current_row - 1
            elif smallest_diff_index == 2:
                current_row = current_row + 1
            # elif smallest_diff_index[0] == smallest_diff_index[2]:
            #     current_row = current_row -1

        current_column = current_column + 1
    map_image.save("elevation_map.png")


find_path(elevation_data)

#         start_point = elevation_data [300][0]
#             #begin the path from the middle of the first column
#             path = []

#         # find_next point with the following
#             #   1) get the elevation at the currnet location. get the current_row from the current_location

#             find_next_point = elevation_data[row][column]

#             # 2) Get the elevations for [row-1][current_column + 1], [row][current_column + 1], [row][current_column + 1]
#             current_location = start_point

#             point_a = elevation_data[row][column + 1]
#             point_b = elevation_data [row - 1][column + 1]
#             point_c = elevation_data[row + 1][column + 1]

#         #  Find the difference between current_elevation and other elevations computed in step 2
#             #  4) Find the smallest of the three differences
#             #  5) Follow the path of the smallest difference by setting the current_row to be either row -1, row , row+1 depending on what you find in 4

#             while current_location < len(elevation_data [0]) and current_location
#                 map_image.putpixel((column, row), (255, 0, 0, 255))

#                 if current_location >= point_a:
#                     find_next_point = point_a
#                 elif point_b <= current_location and point_b < point_c:
#                     find_next_point = point_b
#                 elif point_c <= current_location and point_c < point_b:
#                     find_next_point = point_c
#                 else:
#                     find_next_point = random.randint(point_b, point_c)
#                     path.append(find_next_point)

#                 # 6) Continue from 1 again
#             return path
#             # current_location has to be the start point, from where it goes forward and becomes the next current location

# find_path(elevation_data)
#    def draw_pixel(x,y):

# 1) trace_path (x, y, data)
# 1.5) draw_pixed(x,y)
# 2) Check for min of (data[y][x] - data[y-1][x+1], data[y][x] - data[y][x+1], data[y][x] - data[y+1][x+1])
# 3) trace_path(newpath, data )


# * data to find the next step on our path
# * elevation map data
# * current location of the person

# def find_path(elevation_map_data, starting_location):
#     elevation_map_data: list of lists
#     starting_location == x,y tupples
#     continually call (find-next stop(elevation_map-data, current_location))

# path = (starting_location)
# current_location = starting_location

# while current_location()) < len(elevaton_map_data[0]):
#     next_location = find_next_step(elevation_map_data, current_location)
#     path.append(next_location)

# return path

# for y, row in enumerate(data):
#   for x, num in enumerate(row):
#       img.putpixel(x,y), (num, num, num)

# if i'm at the maximum index don't go beyond it
# current y is equal to maximum y
# which index has this value)

# abs -- absolute value of (x,y) -- use dictionary, or list of tupples
#

# not greater than 0 and less than len; candidates for next step is x plus one and y, y-1 and y +1

# go from east to west in a straight line first

# int(e /max * 255( elevation brightness)
