class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ll = len(strs)
        if ll == 1:
            return strs[0]
        
        mm = min([len(n) for n in strs])
        counter = 0
        holder = ''

        s = 0
        while s < mm:
            for l in range(ll-1):
                if strs[l][s] == strs[l+1][s]:
                    counter += 1
                else:
                    break

            if counter == ll-1:
                holder += strs[0][s]
            else:
                return holder
            counter = 0
            s += 1
        return holder

        # fir = strs[0]
        # keep = []
        # for n in strs[1:]:
        #     keep = list(fir) & list(n) # which is only able on set()
        # return keep