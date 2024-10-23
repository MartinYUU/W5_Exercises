#  You are going to tile a room whose dimensions are length by width feet. There are 
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You 
# can only buy full boxes, not a partial box. 
# You also want to buy 10% more tiles than you need in order to handle chips, breakage, 
# and mess-ups. How many total boxes will you buy? 

import math

roomLength = 25
roomWidth = 20
roomArea = roomLength * roomWidth
tilesPerBox = 12
print('Area of the room is', roomArea)

minBoxes = math.ceil((roomArea / tilesPerBox) * 1.1)
print('A minimum of', minBoxes, 'boxes are needed')
