from scipy import misc
import json


class CoordinateInFishzone:
    def __init__():
        pixel_array = []
	color_legend = {}
        NW = (0,0)
        SE = (0,0)
        
    def coord_to_index(coord):
        x = (coord[1] - self.NW[1])/(self.SE[1] - self.NW[1]) * len(self.pixel_array[0]) 
        y = (coord[0] - self.SE[0])/(self.NW[0] - self.SE[0]) * len(self.pixel_array) 
       
        return int(x),int(y)

    def fishery_prob(coord):
        x,y = self.coord_to_index(coord)
        RGB_value = self.pixel_array[y][x]  # turn tuple into string
        return self.color_legend["RGB_legend"][RGB_value]

    def get_image():
        self.pixel_array = misc.imread('map.png')

    def get_json(json_file_name):
        json_data = open(json_file_name)
        data = json.load(json_data)
        json_data.close()
        
        self.color_legend(

