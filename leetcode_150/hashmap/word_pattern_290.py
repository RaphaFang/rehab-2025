class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        holder = {}
        time = 0
        ll = len(list(pattern))
        ls = s.split()
        if ll!= len(ls):
            return False
        
        if len(set(list(pattern))) != len(set(ls)):
            return False

        while time < ll:
            temp = holder.get(pattern[time],0)
            if temp == 0:
                holder[pattern[time]] = ls[time]
            else:
                if temp != ls[time]:
                    return False
            time += 1
            
        if len(set(holder.keys())) == len(set(holder.values())):
            return True
        return False