class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        hh = list(haystack)
        nn = list(needle)

        hl = 0
        nl = 0

        while hl < len(hh):
            if hh[hl] == nn[nl]:
                nl += 1
                if nl == len(nn):
                    return hl - len(nn) +1
                hl += 1
            else:
                hl = hl -nl +1 # the magical backward... if nl == 0, then nothing happened
                nl = 0


        return -1
    
# but still, simply take the most easiest way 
# return haystack.find(needle)