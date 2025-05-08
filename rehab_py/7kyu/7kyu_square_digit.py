def square_digits(num):
    return int("".join(str(int(n)**2) for n in str(num)))

square_digits(9119)