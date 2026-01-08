class Solution:
    def romanToInt(self, s: str) -> int:
        ns = list(s)
        ll = len(ns)
        start = 0
        dd = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        holder = 0
        while start < ll:
            now = dd[ns[start]]
            if start < ll -1:
                next = dd[ns[start+1]]
                if next > now:
                   holder += (next - now)
                   start +=2
                   continue

            holder += now
            start +=1

        return holder



ss = Solution()
print(ss.romanToInt("LVIII"))