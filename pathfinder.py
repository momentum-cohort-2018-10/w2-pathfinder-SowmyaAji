from PIL import Image, ImageColor
import sys
import random





with open("elevation_small.txt") as text_file:
         
        elevation_data = []
        for line in text_file.readlines():
            elevation_data.append([int(every_number) for every_number in line.strip().split()])

def find_max_elevation(data):
   #find the highest elevation point in the data
    current_max = None
    for line in data:
        line_max = max(line)        
        if current_max is None or line_max > current_max:
            current_max = line_max
    return current_max

max_elevation = find_max_elevation(elevation_data)


def find_min_elevation(data):
    #find the lowest elevation point in the data
    current_min = None
    for line in data:
        line_min = min(line)
        if current_min is None or line_min < current_min:
            current_min = line_min
    return current_min

min_elevation = find_min_elevation(elevation_data)



map_image = Image.new('RGBA',[len(elevation_data[0]),len(elevation_data)])

for row in range(len(elevation_data)):
    for column in range(len(elevation_data[0])):
        figure = elevation_data[row][column]
        bright = int(((figure - min_elevation)/(max_elevation - min_elevation)) * 255)
        map_image.putpixel((column, row), (255, 255, 255, bright ))
# map_image.save("elevation_map.png")



def find_path(elevation_data):
    
    # find the start point and loop through the three options to trace the path along the elevations map
      
    current_row = 300
    current_column = 0
    
        
    while current_column < len(elevation_data[0]) and current_column >= 0:
        
        elevation = elevation_data[current_row][current_column]
        
        map_image.putpixel((current_column,current_row),(255, 0, 0, 255))
        if current_column + 1 < len(elevation_data[0]):
            elevations = [sys.maxsize, sys.maxsize, sys.maxsize]
            if current_row > 0:  
                elevations[0] = elevation_data[current_row - 1][current_column + 1]
            elevations[1] = elevation_data[current_row][current_column + 1]
            if current_row + 1 < len(elevation_data):
                elevations[2] = elevation_data[current_row + 1][current_column + 1]
            
            differences = [abs(elevation - next_elevation) for next_elevation in elevations]
            smallest_diff_index = differences.index(min(differences))

            if smallest_diff_index == 0:
                current_row = current_row -1
            elif smallest_diff_index == 2:  
                current_row = current_row + 1
            elif smallest_diff_index[0] == smallest_diff_index[2]:
                current_row = current_row -1

        current_column = current_column + 1
    map_image.save("elevation_map.png")

find_path(elevation_data)

