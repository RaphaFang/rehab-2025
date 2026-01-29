class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def pattern_l(x):
            temp_dict = {}
            ll = []
            for i in range(len(x)):
                if temp_dict.get(x[i], 0):
                    ll.append(temp_dict[x[i]])

                else:
                    if i == 0:
                        ll.append("a")
                        temp_dict[x[i]] = "a"
                    else:
                        ll.append(i)
                        temp_dict[x[i]] = i
            return ll
        
        if pattern_l(s) == pattern_l(t):
            return True
        return False