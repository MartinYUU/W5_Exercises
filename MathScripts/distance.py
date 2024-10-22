# How do you calculate the distance between coordinates (x1,y1) and (x2,y2)? 
import math
x1 = 1
y1 = 5

x2 = 6
y2 = 2

distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

print ('the distance between coordinates (x1,y1) and (x2,y2) is', round(distance, 2))