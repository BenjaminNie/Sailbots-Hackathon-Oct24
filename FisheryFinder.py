from CoordinateInFishzone import *

class FisheryFinder():
    def __init__(self, array):
    	self.density_array = array
    	self.NW = (0,0)
        self.SE = (0,0)

    def coord_to_index(self, coord):
        x = (coord[1] - self.NW[1])/(self.SE[1] - self.NW[1]) * len(self.density_array[0]) 
        y = (coord[0] - self.SE[0])/(self.NW[0] - self.SE[0]) * len(self.density_array) 
       
        return int(x),int(y)

    def fishery_prob(self,coord):
        x,y = self.coord_to_index(coord)
        return self.density_array[y][x]  # returns tupl

    def get_json(self, json_file_name):
        # load json data
        json_data = open(json_file_name)
        data = json.load(json_data)
        json_data.close()

        # convert string values into floats
        self.NW = string_to_float_tuple(data["NW_coord"])
        self.SE = string_to_float_tuple(data["SE_coord"])