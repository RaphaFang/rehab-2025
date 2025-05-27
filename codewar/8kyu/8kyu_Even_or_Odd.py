def even_or_odd(number):
    return "Even" if number%2==0 else "Odd"

def even_or_odd(number):
    return "Odd" if number&1 else "Even"

# ----------------------------------------------------------------------------
# import timeit
# def even_or_odd():
#     number = 169
#     return "Even" if number%2==0 else "Odd"

# def even_or_odd_op():
#     number = 169
#     return 'Odd' if number & 1 else 'Even'


# time_original = timeit.timeit(even_or_odd, number=100000)
# time_optimized = timeit.timeit(even_or_odd_op, number=100000)
# 0.005748990006395616 0.004978671990102157


# ----------------------------------------------------------------------------
# !1.
# bitwise operators
# 比較二進制位元，＆是取出兩者交集的對應位元，例如5 -> 101, 6 -> 110
# 會得到100，也就會是4
# 快速的判斷是否是特定偶數的倍數，例如2, 4, 8的倍數
# 或是設定權限如下方

# READ = 0b0001
# WRITE = 0b0010
# EXECUTE = 0b0100

# user_permission = READ | EXECUTE
# if user_permission & WRITE:
#     print("可寫入")
# else:
#     print("不能寫入")
