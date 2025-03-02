#ask a VA, Ask a virtual assistant
### the modulus operator finds the remainder after division and
### checking divisibility, extracting digits from a number, and
###clock arithmatic. 2. XOR is a logical operation that returns true
###if exactly one of the operands is true but not BOTH.
#nested
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
        pass


#chained conditional
if x == y:
    print('x and y are equal')
elif x < y:
    print('x is less than y')
else:
    print('x is greater than y'
          pass


#rewrite using a conditional using a single condition
#nested conditional
    if 0 < x:
        if
    x < 10: \
        print('x is a positive single-digit number.')
    pass


#simplified version
    if 0 < x < 10:
        print('x is a positive single-digit number.')
        pass


#simplify unnecessary complex condition
#if not x <= 0 and not x >= 10:
    print('x is a positive single-digit number.')
    pass


#simplified
    if 0 < x < 10:
        print('x is a positive single-digit number.')


#fixed countdown


    def countdown_by_two(n):
        if n <= 0:  # Change condition to prevent infinite recursion
            print('Blastoff!')
        else:
            print(n)
            countdown_by_two(n - 2)

        # Test cases


    countdown_by_two(6)  # 6, 4, 2, Blastoff!
    countdown_by_two(7)  # 7, 5, 3, 1, Blastoff!


