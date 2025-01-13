class Solution:
    def minimumLength(self, s: str) -> int:
        hmap = {}
        for char in s:
            hmap.setdefault(char, 0)
            hmap[char] += 1

        removed = 0
        for key in hmap:
            hmap[key] += hmap[key] % 2
            removed += hmap[key]-2
        return len(s) - removed


s = "abaacbcbb"
output = 5

obj = Solution()
res = obj.minimumLength(s)
print(res)
print(output)
print(res == output)
