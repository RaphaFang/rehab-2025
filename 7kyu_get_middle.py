def get_middle(s):
    ll = len(s)
    if ll&1:
        index1 = (ll-1)//2
        return (s[index1])
    else:
        index1= (ll//2)-1
        return (s[index1:index1+2:])

def get_middle(s):
    return s[(len(s)-1)//2:len(s)//2+1]


# ------------------------------------------------------------------
# import timeit
# def op():
#     s = "aaaaaaaa"
#     ll = len(s)
#     return s[(ll-1)//2:ll//2+1]

# def get_middle():
#     s = "aaaaaaaa"
#     ll = len(s)
#     if ll&1:
#         index1 = (ll-1)//2
#         return (s[index1])
#     else:
#         index1= (ll//2)-1
#         return (s[index1:index1+2:])

# time_optimized = timeit.timeit(op, number=1000000)
# time_original = timeit.timeit(get_middle, number=1000000)
# print(time_original,time_optimized)
# 0.11125326598994434 0.163226194010349

# ! 奇數情況下，我的寫法可以跳過直接index呼叫
# 偶數情況下，兩者速度是相同的