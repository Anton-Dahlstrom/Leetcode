from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for word in words:
            cur = 0
            for char in word:
                num = ord(char) - ord("a")
                val = weights[num]
                cur += val
                cur %= 26
            cur = 26-cur-1
            res += chr(cur+ord("a"))

        return res


words = ["abcd", "def", "xyz"]
weights = [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6,
           9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]
output = "rij"

obj = Solution()
res = obj.mapWordWeights(words, weights)
print(res)
print(output)
print(res == output)
