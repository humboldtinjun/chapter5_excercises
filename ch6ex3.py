def is_between(x, y, z):
    return x <= y <= z or x >= y >=z
print(is_between(1, 2, 3))  # True
print(is_between(3, 2, 1))  # True
print(is_between(1, 3, 2))  # False
print(is_between(2, 2, 2))  # True
