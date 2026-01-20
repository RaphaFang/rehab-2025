class Solution:
    def trailingZeroes(self, n: int) -> int:
        rr = 0
        while n:
            n //= 5
            rr += n
        return rr

    
    # --------FIRST-TRY--------
    def trailingZeroes(self, n: int) -> int:
        g2, g5 = 0, 0
            
        def factor(n):
            is_2 = 0
            is_5 = 0
            gogo = True
            while gogo:
                if n % 2 == 0:
                    is_2 += 1
                    n /= 2
                else:
                    if n % 5 == 0:
                        is_5 += 1
                        n /= 5
                    else:
                        gogo = False
            return is_2, is_5

        
        for _ in range(1, n+1):
            n2, n5 = factor(_)
            g2 += n2
            g5 += n5
        return min(g2, g5)
    
        # ----- FAIL -----
        # is_2 = 0
        # is_5 = 0
        # for _ in range(1, n+1):
        #     if _ == 2:
        #         is_2 += 1
        #     if _ == 5:
        #         is_5 += 1
        # return min(is_2, is_5)

        # ----- FAIL -----
        # holder = factorint(n)
        # print(holder)
        # return min(holder.get(2,0), holder.get(5,0))
        # ----- FAIL -----
        # h = 1
        # rr = 0
        # for _ in range(1, n+1):
        #     h *= _
        #     print(h)
        #     if h % 10 == 0:
        #         print(h)
        #         h /= 10
        #         rr += 1
        # return rr
    
        # ----- FAIL -----
        # h = 1
        # for _ in range(1, n+1):
        #     h *= _
        # hh = str(h)[::-1]
        # rr = 0
        # for n in hh:
        #     if n == "0":
        #         rr += 1
        # return rr


