from CoordinateInFishzone import *
import FisheryFinder

config_file = 'config.txt'

zone = CoordinateInFishzone()
zone.get_json(config_file)
zone.get_image()
prob_array = zone.convert_image()
#print prob_array

fishFinder = FisheryFinder.FisheryFinder(prob_array)
fishFinder.get_json(config_file)

prob = fishFinder.fishery_prob( (52.97, -9.97) )

print "Probability of fishing zone is " + str(prob)