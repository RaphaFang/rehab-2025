def monkey_count(n):
    result_list = []
    for i in range(1,n+1):
        result_list.append(i)   
    return result_list

def monkey_count_optimized(n):
    return [i for i in range(1,n+1)]

def monkey_count_optimized_second(n):
    return list(range(1,n+1))

# import timeit
# def monkey_count_op_first():
#     return [i for i in range(1,2000)]

# def monkey_count_op_second():
#     return list(range(1, 2000))

# ff= timeit.timeit(monkey_count_op_second, number=1000000)
# ss = timeit.timeit(monkey_count_op_second, number=1000000)
# 33.41426449399842 32.991611061001095