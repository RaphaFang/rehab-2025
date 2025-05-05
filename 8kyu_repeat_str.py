def repeat_str(repeat, string):
    return "".join(string for n in range(0,repeat))

def repeat_str(repeat, string):
    return repeat * string
# ----------------------------------------------------------------------------
# !只能int*str 反過來會報錯

# import timeit
# def repeat_str_1():
#     repeat, string = 10, "aaa_"
#     return "".join(string for n in range(0,repeat))

# def repeat_str_2():
#     repeat, string = 10, "aaa_"
#     return repeat * string


# time_ori = timeit.timeit(repeat_str_1, number=100000)
# time_opt = timeit.timeit(repeat_str_2, number=100000)

# print(time_ori, time_opt)
# 0.09346470499440329 0.010097600999870338