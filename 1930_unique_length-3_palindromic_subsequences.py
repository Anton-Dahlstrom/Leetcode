class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}
        res = 0
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            else:
                last[char] = i
        for char in last:
            res += len(set(s[first[char]+1:last[char]]))
        return res


s = "bbcbaba"
output = 4

obj = Solution()
res = obj.countPalindromicSubsequence(s)
print(res)
print(output)
print(res == output)
