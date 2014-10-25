from scipy import misc
import json


class CoordinateInFishzone():
    def __init__(self):
        self.pixel_array = []
        self.color_legend = {}
        self.NW = (0,0)
        self.SE = (0,0)
        
    def coord_to_index(self, coord):

        print (coord[1])
        print (coord[0])

        x = (coord[1] - self.NW[1])/(self.SE[1] - self.NW[1]) * len(self.pixel_array[0]) 
        y = (coord[0] - self.SE[0])/(self.NW[0] - self.SE[0]) * len(self.pixel_array) 
       
        return int(x),int(y)

    def fishery_prob(self,coord):
        x,y = self.coord_to_index(coord)
        RGB_value = self.pixel_array[y][x]  # tuple

        print (RGB_value)
        return self.color_legend[RGB_value]

    def get_image(self):
        self.pixel_array = misc.imread('map.png')

    def get_json(self, json_file_name):
        json_data = open(json_file_name)
        data = json.load(json_data)
        json_data.close()
        pre_legend = data["RGB_legend"]
        for string_key in pre_legend:
            t = string_to_int_tuple(string_key)
            self.color_legend[t] = pre_legend[string_key]
        self.NW = string_to_float_tuple(data["NW_coord"])
        self.SE = string_to_float_tuple(data["SE_coord"])

def string_to_int_tuple(string):
    return tuple([int(x) for x in string.strip('(').strip(')').split(',')])

def string_to_float_tuple(string):
    return tuple([float(x) for x in string.strip('(').strip(')').split(',')])


"""
from test import *
zone = CoordinateInFishzone()
zone.get_json('config.txt')
zone.get_image()
"""
