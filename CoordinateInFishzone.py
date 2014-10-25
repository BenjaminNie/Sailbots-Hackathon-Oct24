from scipy import misc
from PIL import Image
import numpy as np
import json
import sys
import scipy

class CoordinateInFishzone():
    def __init__(self):
        self.pixel_array = []
        self.color_legend = {}

    def fishery_prob(self, x, y):
        RGB_value = self.pixel_array[y][x]  # returns tuple
        try:
            return self.color_legend[tuple(RGB_value[0:3])]  # take element 0-2 of tuple as key
        except:
            smallest_dist = sys.maxsize+1
            smallest_dist_value = sys.maxsize+1
            for key in self.color_legend.keys():
                color_distance = ((RGB_value[0]-key[0])**2+(RGB_value[1]-key[1])**2+(RGB_value[2]-key[2])**2)
                if color_distance < smallest_dist:
                    smallest_dist = color_distance
                    smallest_dist_value = self.color_legend[key]
            return smallest_dist_value

    def get_image(self):
        self.pixel_array = misc.imread('map.png')

    def get_json(self, json_file_name):
        # load json data
        json_data = open(json_file_name)
        data = json.load(json_data)
        json_data.close()

        # convert string legend into tuple legend
        pre_legend = data["RGB_legend"]
        for string_key in pre_legend:
            t = string_to_int_tuple(string_key)
            self.color_legend[t] = pre_legend[string_key]

    def convert_image(self):
        self.output = misc.imread('map.png')
        print len(self.output)
        print len(self.output[0])
        array_of_nums = []
        for i in range(0, len(self.output)-1):
            array_of_nums.append([])
            for j in range(0, len(self.output[0]-1)):
                val = self.fishery_prob(j, i)
                self.output[i][j] = val
                array_of_nums[i].append(val)
        #scipy.misc.imsave('outfile.png', output)
        self.output = Image.fromarray(np.uint8(self.output))
        self.output.save('out.png')
        #print array_of_nums
        return array_of_nums

def string_to_int_tuple(string):
    return tuple([int(x) for x in string.strip('(').strip(')').split(',')])

def string_to_float_tuple(string):
    return tuple([float(x) for x in string.strip('(').strip(')').split(',')])


"""
from CoordinateInFishzone import *
zone = CoordinateInFishzone()
zone.get_json('config.txt')
zone.get_image()
zone.convert_image()
zone.fishery_prob( (55, -15) )
zone.fishery_prob_test(429, 128)
"""
