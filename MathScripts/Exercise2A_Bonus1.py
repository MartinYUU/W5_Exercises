# I will be rewriting the area of a circle exercise to use the input() function
import math
circleRadius = int(input('What is the radius of your circle: '))

circArea = math.pi * (math.pow(circleRadius, 2))

print('The area of a circle with radius', circleRadius, 'is', circArea)