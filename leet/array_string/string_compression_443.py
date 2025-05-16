from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        counter = 1
        for i in range(len(chars)):
            if i<len(chars)-1 and chars[i] == chars[i+1]:
                counter+=1
            else:
                result.append(chars[i])
                if counter > 1:
                    result.extend(list(str(counter)))
                counter = 1

        
        chars.clear()
        chars.extend(result)
        return len(result)
    
    # ---------------------------------------------------------------
    # 下面這作法出問題在於他會一次count()全部的內容物
    def compress(self, chars: List[str]) -> int:
        result = []
        for n in chars:
            if n not in result:
                temp = chars.count(n)
                result.append(n)
                if temp != 1:
                    print(list(str(temp)))
                    result.extend(list(str(temp)))
        
        chars.clear()
        chars.extend(result)
        return len(result)


aa = Solution()
print(aa.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))


# print(result.items()) 會得到
# dict_items([('a', 2), ('b', 2), ('c', 3)])