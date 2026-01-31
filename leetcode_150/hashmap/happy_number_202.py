class Solution:
    def isHappy(self, n: int) -> bool:
        ln = list(str(n))
        time = 10
        while time:
            nnl = [int(n)**2 for n in ln]
            temp = sum(nnl)
            if temp in {1, 19, 82, 68, 100}:
                return True

            ln = list(str(temp))
            time -= 1
        return False