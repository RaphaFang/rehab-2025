def positive_sum(arr):
    return sum([n for n in arr if n >0])

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# ----------------------------------------------------------------------------
# ! list comprehension vs generator expression
# 兩者在小資料量上差異不代，但是list變大，就有差

# import timeit
# def positive_sum_1():
#     arr = list(range(-10_000, 10_000))
#     return sum([n for n in arr if n >0])

# def positive_sum_2():
#     arr = list(range(-10_000, 10_000))
#     return sum(x for x in arr if x > 0)

# ff = timeit.timeit(positive_sum_1, number=100)
# ss = timeit.timeit(positive_sum_2, number=100)

# print(ff,ss)
# 0.08756324099886115 0.09390460999929928