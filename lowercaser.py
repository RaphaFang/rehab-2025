def lowercaser(item, quize_id):
    print(item.lower().replace(" ", "_") + "_" + str(quize_id) + ".")
        

lowercaser("Find Users With Valid E-Mails", 1517)


# ----------------------------------------------------------------------------
# 特定情況中replace還是最快的
# ! lower().replace() (2-pass): 0.004274042003089562
# ! Original for-loop: 0.1643432079872582
# ! Comprehension (1-pass): 0.20072483300464228


# import timeit
# def method_original(item, id): 
#     ll = []
#     for n in item:
#         if n != " ":
#             ll.append(n.lower())
#         else:
#             ll.append("_")
#     return "".join(ll)+ str(id)

# def method_comprehension(item, id): 
#     return "".join('_' if c == ' ' else c.lower() for c in item) + str(id)

# def method_replace(item, id): 
#     return item.lower().replace(" ", "_")+ str(id)

# item = "This is a Test String With Multiple Words and SPACES" * 1000
# id = 1581

# 這邊用lambda，是因為原先不能塞入元件到要測試的函數中
# print("Original for-loop:", timeit.timeit(lambda: method_original(item, id), number=100))
# print("Comprehension (1-pass):", timeit.timeit(lambda: method_comprehension(item, id), number=100))
# print("lower().replace() (2-pass):", timeit.timeit(lambda: method_replace(item, id), number=100))
