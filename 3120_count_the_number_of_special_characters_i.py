class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small = set()
        big = set()
        for char in word:
            if ord(char) < 97:
                big.add(char)
            else:
                small.add(char)
        res = 0
        for char in big:
            mirror = chr(ord(char) + 32)
            if mirror in small:
                res += 1
        return res
