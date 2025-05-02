def remove_exclamation_marks(s):
    output_s = ""
    for n in list(s):
        if n.isalpha() or n==" " or n==",":
            output_s+=n
    return output_s

def remove_exclamation_marks(s):
    return "".join(n for n in s if n.isalpha() or n in {" ", ","})

def remove_exclamation_marks(s):
    return s.replace("!", "")

# test ----------------------------------------------------------------------------
# import timeit
# def remove_exclamation_marks_original():
#     s = "Hello World!!! " * 100
#     output_s = ""
#     for n in list(s):
#         if n.isalpha() or n == " " or n == ",":
#             output_s += n
#     return output_s

# def remove_exclamation_marks_optimized():
#     s = "Hello World!!! " * 100
#     return "".join(n for n in s if n.isalpha() or n in {" ", ","})

# time_original = timeit.timeit(remove_exclamation_marks_original, number=10000)
# time_optimized = timeit.timeit(remove_exclamation_marks_optimized, number=10000)
# 1.4191387750033755 1.0589974290051032


# ----------------------------------------------------------------------------
# !1.
# mutable immutable 可變與不寫變得變數
# 因為在immutable上用到+=，實際上是複製舊的，變化，再重新賦予數值
    # str，會是複製一大串（如果字串很大），加上變化，「建立新的物件」，重新賦予數值
    # int，上效能不影響，也會複製（但是數字的byte佔用小），運算，「建立新的物件」，重新賦予數值
# 避免，要改用mutable 的 list來處理

# !2.
# 查找用hash table效率高
# dict（key value correspond） set（key） 都是，list 不是

# !3.
# Regular Expression
# 正規表達式，像是我之前檢查是否為有效email的方式，透過一個咒語一般的方式檢驗，避免編寫麻煩的條件
# 可以同時定義多條件，以及找到多目標


# ----------------------------------------------------------------------------
# s = ""
# s += "a"  → id: 139332946360544
# s += "b"  → id: 139332860719488  ❗不同
# s += "c"  → id: 139332860726464  ❗不同
# lst = []
# lst.append("a") → id: 139332861261584
# lst.append("b") → id: 139332861261584  ✅ 相同
# lst.append("c") → id: 139332861261584  ✅ 相同