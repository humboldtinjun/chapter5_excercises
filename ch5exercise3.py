#triangle test
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("yes") #valid triangle
    else: print("no") #invalid triangle

is_triangle(3, 4, 5)
is_triangle(3, 1, 5)

