def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# test
print(gcd(48, 18))  # Output 6
print(gcd(56, 98))  # Output 14
print(gcd(101, 103))  # Output 1
print(gcd(270, 192))  # Output 6

