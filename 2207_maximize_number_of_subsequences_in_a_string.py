class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        n = len(text)
        res = 0
        left = 0
        right = 0
        for i in range(n):
            if text[i] == pattern[1]:
                res += left
                right += 1
            if text[i] == pattern[0]:
                left += 1
        res += max(left, right)
        return res


text = "abdcdbc"
pattern = "ac"
output = 4


obj = Solution()
res = obj.maximumSubsequenceCount(text, pattern)
print(res)
print(output)
print(res == output)
