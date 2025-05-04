def make_negative_1():
    number = 100
    return -number if number>0 else number

def make_negative_2():
    number = 100
    return -abs(number)


# import timeit as tt
# aa = tt.timeit(make_negative_1, number=100000)
# bb = tt.timeit(make_negative_2, number=100000)
# print(aa,bb)

# 0.006561571000929689 0.007014388000243343