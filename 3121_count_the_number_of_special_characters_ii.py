from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        big = set()
        found = defaultdict(int)
        for char in word:
            if char.islower():
                if chr(ord(char)-32) in big:
                    found[char] = 0
                else:
                    found[char] = 1
            else:
                big.add(char)

        res = 0
        for char in found:
            if chr(ord(char)-32) in big:
                res += found[char]

        return res
