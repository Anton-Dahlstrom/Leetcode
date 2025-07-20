class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n-1
        while l < r:
            char = s[l]
            if s[r] != char:
                break
            while l <= r and s[l] == char:
                l += 1
            while l <= r and s[r] == char:
                r -= 1
        return r-l+1


s = "cabaabac"
output = 0

obj = Solution()
res = obj.minimumLength(s)
print(res)
print(output)
print(res == output)
