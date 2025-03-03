def ackerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackerman(m - 1, 1)
    else:
        return ackerman(m - 1, ackerman(m, n - 1))

# Example test cases
print(ackerman(0, 0))  # Output: 1
print(ackerman(1, 1))  # Output: 3
print(ackerman(2, 2))  # Output: 7
print(ackerman(3, 3))  # Output: 61