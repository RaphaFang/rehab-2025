class Solution:
    def guessNumber(self, n: int) -> int:
        s, e= 1, n

        while True:
            test = (s+e)//2
            r = guess(test)

            if r==0:
                return test
            elif r > 0:
                s = test +1
            elif r < 0:
                e = test -1

# ! TLE
# ! overflow 
# int test = (s + e) / 2;
# 如果整數過大，這樣相加會超過導致永不為0，我就超時了
# int 是 固定 32-bit 帶正負號的整數，範圍是 -2^31 ~ 2^31 - 1（即 -2147483648 ~ 2147483647）
# 即使超過 32-bit、甚至 64-bit，Python 會自動轉換成更大的表示法，繼續運算，不會溢位。