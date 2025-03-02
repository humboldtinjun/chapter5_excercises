#stack diagram
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

recurse(3, 0)
pass
#stack diagram
recurse(3, 0)  → calls recurse(2, 3)
    recurse(2, 3)  → calls recurse(1, 5)
        recurse(1, 5)  → calls recurse(0, 6)
            recurse(0, 6)  → Prints "6" and returns
        recurse(1, 5)  → Returns
    recurse(2, 3)  → Returns
recurse(3, 0)  → Returns

#the output is 6 
