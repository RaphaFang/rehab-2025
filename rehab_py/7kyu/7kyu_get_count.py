def get_count(sentence):
    num = 0
    for n in sentence:
        if n in {"a", "e", "i", "o", "u"}:
            num += 1
    return num


# def get_count(sentence):
#     return sum(1 for n in sentence if n in {"a", "e", "i", "o", "u"})



# ----------------------------------------------------------------------------
# def get_count_1():
#     sentence = "bcdfghjklmnpqrstvwxz y"
#     num = 0
#     for n in sentence:
#         if n in {"a", "e", "i", "o", "u"}:
#             num += 1
#     return num


# def get_count_2():
#     sentence = "bcdfghjklmnpqrstvwxz y"
#     return sum(1 for n in sentence if n in {"a", "e", "i", "o", "u"})


# import timeit

# aa = timeit.timeit(get_count_1, number=100000)
# bb = timeit.timeit(get_count_2, number=100000)

# print(aa,bb)
# 0.052385032999154646 0.0742107420010143