from PIL import Image, ImageColor
import sys
import random
import pytest

# pathfinder program using a class and a global function


def get_data():
    """get elevations data from the txt file"""
    with open("elevation_small.txt") as text_file:

        elevation_data = []
        for line in text_file.readlines():
            elevation_data.append([int(every_number)
                                   for every_number in line.strip().split()])
        return elevation_data


class Map:

    def __init__(self, data):
        self.data = data

    def _find_max_elevation(self):
        """find the highest elevation point in the data"""
        current_max = None
        for line in self.data:
            line_max = max(line)
            if current_max is None or line_max > current_max:
                current_max = line_max
        return current_max

    def _find_min_elevation(self):
        """find the lowest elevation point in the data"""
        current_min = None
        for line in self.data:
            line_min = min(line)
            if current_min is None or line_min < current_min:
                current_min = line_min
        return current_min

    def create_map(self):
        """draw the map of the elevations assigning it the white to black color range"""
        min_elevation = self._find_min_elevation()
        max_elevation = self._find_max_elevation()
        map_image = Image.new('RGBA', [len(self.data[0]), len(self.data)])

        for row in range(len(self.data)):
            for column in range(len(self.data[0])):
                figure = self.data[row][column]
                bright = int(((figure - min_elevation) /
                              (max_elevation - min_elevation)) * 255)
                map_image.putpixel((column, row), (bright, bright, bright))

        # map_image
        return map_image

    def find_path(self):
        """calculate the three different elevations the path can take to go forward, compute the smallest of the three and create the path across the mountains, beginning in the middle of the first column"""
        current_row = 300
        current_column = 0
        map_image = self.create_map()
        while current_column < len(self.data[0]) and current_column >= 0:
            elevation = self.data[current_row][current_column]
            map_image.putpixel((current_column, current_row), (255, 0, 0, 255))
            if current_column + 1 < len(self.data[0]):
                elevations = [sys.maxsize, sys.maxsize, sys.maxsize]
                if current_row > 0:
                    elevations[0] = self.data[current_row -
                                              1][current_column + 1]
                elevations[1] = self.data[current_row][current_column + 1]
                if current_row + 1 < len(self.data):
                    elevations[2] = self.data[current_row +
                                              1][current_column + 1]

                differences = [abs(elevation - next_elevation)
                               for next_elevation in elevations]
                smallest_diff_index = differences.index(min(differences))

                if smallest_diff_index == 0:
                    current_row = current_row - 1
                elif smallest_diff_index == 2:
                    current_row = current_row + 1

            current_column = current_column + 1
        map_image.save("elevation_map.png")


if __name__ == '__main__':
    map_im = Map(get_data())
    map_im.find_path()
