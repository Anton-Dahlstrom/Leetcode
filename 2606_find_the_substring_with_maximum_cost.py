class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        n = len(s)
        hmap = {}
        for i, char in enumerate(chars):
            hmap[char] = vals[i]
        cur = 0
        res = 0
        for i in range(n):
            cur = max(0, cur)
            char = s[i]
            if char in hmap:
                cur += hmap[char]
            else:
                cur += ord(char) - 96
            res = max(cur, res)
        return res


s = "adaa"
chars = "d"
vals = [-1000]
output = 2

s = "xuusmmums"
chars = "sxmu"
vals = [-6, 5, 0, 5]
output = 15

obj = Solution()
res = obj.maximumCostSubstring(s, chars, vals)
print(res)
print(output)
print(res == output)
