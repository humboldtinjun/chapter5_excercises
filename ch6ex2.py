#def hypot in incremental steps
def hypot(a, b):
    return 0.0
    pass#placeholder return value
#print(hypot(3, 4))

def hypot(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    print(f"a_squared: {a_squared}, b_squared: {b_squared}")
    return 0.0
pass
#print(hypot(3, 4))

def hypot(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    sum_squares = a_squared + b_squared
    print(f"sum_squares: {sum_squares}")
    return 0.0
pass
#print(hypot(3, 4))

import math
def hypot(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    sum_squares = a_squared + b_squared
    hypotenuse = math.sqrt(sum_squares)
    print(f"hypotenuse: {hypotenuse}")
    return 0.0
print(hypot(3, 4))
print(hypot(5, 12))


