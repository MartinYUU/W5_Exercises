# Description: This script tests various numeric conversion techniques 
# Author: Martin Reyes

# ∗ Cast as integer using int()  
# ∗ Cast as float using float()  
# ∗ For variable a, try casting into a float then integer, like this: int(float(a))  
# Page 51 of 87 
# Data Analyst Academy Week 5  
# Student Guide 
# ∗ Use slicing to add just the numeric portion of the string to a new variable 
# (remember, indexing always starts with 0!), and cast the number as an integer or 
# string, whichever is appropriate 
# ∗ For variables a and d, use the .strip() method to remove the leading/trailing 
# spaces.


a = "  101.1 " 
b = '55' 
c = "402 Stevens" 
d = 'Number 5  ' 


# A = int(a) ValueError: invalid literal for int() with base 10: '  101.1 '
B = int(b)
print(B)
# C = int(c) ValueError: invalid literal for int() with base 10: '402 Stevens'
# D = int(d) ValueError: invalid literal for int() with base 10: 'Number 5  '

A = float(a)
print(A)
B = float(b)
print(B)
# C = float(c) ValueError: could not convert string to float: '402 Stevens'
# D = float(d) ValueError: could not convert string to float: 'Number 5  '

A = int(float(a))

A = a[2:7]
str(A)
print(A)
B = b[0:3]
int(B)
print(B)
C = c[0:4]
int(C)
print(C)
D = d[7:9]
int(C)
print(D)

A = a.strip()
print(A)
D = d.strip()
print(D)