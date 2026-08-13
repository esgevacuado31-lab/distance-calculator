

import math

# ask the user to enter the first coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

#ask the user to enter the second coordinates
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute the distance
d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

#Display the result
print("The distance between the two points is:", d)

"""
the math library helped me simplify my program by creating shorter equations for long and complex problems. 
The functions that were easier to use beacuase of the library  were the sqrt and pow since they simplified
the actual process or eqation of square roots and exponents.  
