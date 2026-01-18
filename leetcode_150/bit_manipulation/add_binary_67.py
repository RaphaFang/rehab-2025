class Solution:
    def addBinary(self, a: str, b: str) -> str:
        nn = int(a,2) + int(b,2)
        return str(bin(nn)[2:])
        