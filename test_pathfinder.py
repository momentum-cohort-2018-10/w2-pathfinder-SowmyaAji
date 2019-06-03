import pytest

from pathfinder import find_max_elevation, find_min_elevation


numbers = [[3, 2, 7], [5, 1, 4], [8, 9, 6]]   

def test_get_max_elevation():
    assert find_max_elevation(numbers) == 9

def test_get_max_elevation_of_negative_numbers():
    assert find_max_elevation([[-1, -3], [-2, -4]]) == -1

def test_get_min_elevation():  
    assert find_min_elevation(numbers) == 1

