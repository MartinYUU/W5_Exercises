#  Create a script named min_max.py that displays both the smallest and then the 
# largest of three numbers. 
# Name your variables a, b, and c and assign them values. Then use if/else statements 
# to determine and display the answer. 
# Be sure to test your script using an assortment of different values in your variables, so 
# that you look at a variety of different number combinations.

a = -664
b = 194
c = 456


if a < b and a < c:
    print('min is', a)
elif b < a and b < c:   
    print('min is', b)
else:
    print('min is', c)

if a > b and a > c:
    print('max is', a)
elif b > a and b > c:
    print('max is', b)
else:
    print('max is', c)