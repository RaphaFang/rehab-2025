def cap_me(arr):
    result = [n[:1:].upper()+n[1::].lower() for n in arr]
    return result


def cap_me(arr):
    return list(map(str.capitalize, arr))

# map(函數, 可迭代物件)
# map(function, iterable)
