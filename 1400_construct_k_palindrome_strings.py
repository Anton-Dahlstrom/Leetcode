class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if s == k:
            return True
        elif len(s) < k:
            return False

        chars = set()
        pairs = 0
        for char in s:
            if char in chars:
                pairs += 1
                chars.remove(char)
            else:
                chars.add(char)
        singles = len(s) - pairs*2
        if singles > k:
            return False
        return True


s = "annabelle"
k = 2
output = True

s = "leetcode"
k = 3
output = False

obj = Solution()
res = obj.canConstruct(s, k)
print(res)
print(output)
print(res == output)
