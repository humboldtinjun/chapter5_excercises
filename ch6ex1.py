#ask VA
def absolute_value_wrong(x):
    if x < 0:
        return -x
    if x > 0:
        return x
    pass
###this function does not handle x == 0
def absolute_value_fixed(x):
    if x < 0:
        return -x
    else:  # Handles both `x == 0` and positive numbers
        return x

#Dead Code
def absolute_value_extra_return(x):
    if x < 0:
        return -x
    else:
        return x

    return 'This is dead code.'
pass
### this code is wrong because the last statement wil never be reached.

#unnecessary condition
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
pass
### if already gives you true or false, the else statement is redundant
 # correct distance function
import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)

# Example usage:
print(distance(1, 2, 4, 6))  # Should return 5.0
### it matches
