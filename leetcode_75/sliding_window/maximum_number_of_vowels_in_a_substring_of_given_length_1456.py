class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(('a', 'e', 'i', 'o', 'u'))

        left, right = 0, k-1
        temp = sum(1 for i in range(left, right+1) if s[i] in vowel)
        m_vowel = temp

        while right < len(s) -1:
            if s[left] in vowel:
                temp -= 1
            left += 1

            right +=1
            if s[right] in vowel:
                temp += 1

            m_vowel = max(m_vowel, temp)
        return m_vowel
# ------------------------------------------------------------
# 這超時了
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(('a', 'e', 'i', 'o', 'u'))
        ll = list(s)

        left, right, m_vowel = 0, k, 0
        # temp = []

        while right < len(ll)+1:
            temp = 0
            for i in range(left, right):
                if ll[i] in vowel:
                    temp +=1
            left += 1
            right +=1
            m_vowel = max(m_vowel, temp)
        return m_vowel