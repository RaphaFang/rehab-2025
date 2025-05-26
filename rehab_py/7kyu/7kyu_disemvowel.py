# def disemvowel(string_):
#     return "".join(n for n in string_ if n not in {"a","e","i","o","u","A","E","I","O","U"})

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

table = str.maketrans('', '', 'aeiouAEIOU')
def disemvowel_3_opt():
    string = "No offense but,\nYour writing is among the worst I've ever read"*100
    return string.translate(table)

# ---------------------------------------------------
# !匿名set
# return "".join(n for n in string_ if n not in {"a","e","i","o","u","A","E","I","O","U"})
# 我在這邊做的是匿名set，就會出現重新建立，使用，砍掉
# 但實測，差異不大
# 2.8984252189984545 
# 2.7889936249994207

# ! 直接return "".join(n f....
# 這反而比你獨立寫一行慢..
# 1.7961876399931498
# 2.7877118769974913

# ! translate() 是 C-level 實作，效能極高
# 即便是獨立的哈西表，還是要加上「計算哈西直」的時間
# | 比較項         | `set` 查找                | `translate()` 查找      |
# | ----------- | ----------------------- | --------------------- |
# | 時間複雜度       | **O(1)**（平均，hash table） | **O(1)**（固定表查找）       |
# | 是否需要計算 hash | ✅ 是，每次都會 `hash(obj)`    | ❌ 否，直接查表（類似 array 索引） |
# | 效能差異        | 每次都 `hash + 比對`         | 單純索引表，快一點點            |

# ! set 的成本 除了計算，還有hash collision 
# 兩個算出來同個哈西直，就需要下一步處理

# !但是最通用還是replace，translate只能單char
# | 比較維度     | `translate()`       | `replace()`                   |
# | -------- | ------------------- | ----------------------------- |
# | 功能限制     | 只能處理「單一字元」          | 可以處理任意長度字串                    |
# | 支援條件替換   | ❌ 不行                | ✅ 可以搭配多次 `.replace()`         |
# | 可讀性      | 較低（需搭配 `maketrans`） | 很直覺（"abc".replace("a", "x")）  |
# | 初學者友好程度  | 較難理解                | ✅ 非常簡單                        |
# | 效能       | 🥇 超快（固定映射表）        | 🥈 快，但每次掃整段字串                 |
# | 批次替換多個字串 | ❌ 要自己設計表格／拆解        | ✅ 可多次 replace() 或用 `re.sub()` |



# 查找行為有一點點不同
# dict[key]：
# 對 key 做 hash() → 找到槽位（bucket）
# 只需比對 key
# 查到 key → 直接回傳 value，不再看值

# key in set：
# 對 key 做 hash() → 找到槽位
# 比對 key → 還要確認 value 是 None（或 set 的特殊處理）
# 雖然兩者理論上相同，但因為 set 是 dict 的子集，多了一層封裝與邏輯判斷
# ---------------------------------------------------

vowels = {"a","e","i","o","u","A","E","I","O","U"}
def disemvowel_1():
    string_ = "No offense but,\nYour writing is among the worst I've ever read"*100
    aa = [n for n in string_ if n not in {"a","e","i","o","u","A","E","I","O","U"}]
    return "".join(aa)

def disemvowel_2():
    s = "No offense but,\nYour writing is among the worst I've ever read"*100
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

def disemvowel_3():
    string = "No offense but,\nYour writing is among the worst I've ever read"*100
    return string.translate({ord(i):None for i in 'aeiouAEIOU'})

table = str.maketrans('', '', 'aeiouAEIOU')
def disemvowel_3_opt():
    string = "No offense but,\nYour writing is among the worst I've ever read"*100
    return string.translate(table)

def disemvowel_1_opt():
    string_ = "No offense but,\nYour writing is among the worst I've ever read"*100
    return "".join(n for n in string_ if n not in vowels)

import timeit

aa = timeit.timeit(disemvowel_1, number=10000)
bb = timeit.timeit(disemvowel_2, number=10000)
cc = timeit.timeit(disemvowel_3, number=10000)
dd = timeit.timeit(disemvowel_3_opt, number=10000)
ee = timeit.timeit(disemvowel_1_opt, number=10000)

print(aa,bb,cc, dd, ee)

# 1.7961876399931498
# 0.5312872500071535 
# 0.1306077000044752 
# 0.13411361700855196 
# 2.7889936249994207