class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            biggest = 0
            found = 0
            valid = 0
            hmap = {}
            for j in range(i, n):
                char = s[j]
                if char not in hmap:
                    hmap[char] = 1
                    found += 1
                else:
                    hmap[char] += 1

                if biggest < hmap[char]:
                    biggest = hmap[char]
                    valid = 1
                elif biggest == hmap[char]:
                    valid += 1
                if found == valid:
                    res = max(res, j-i+1)

        return res


s = "zzabccy"
output = 4

obj = Solution()
res = obj.longestBalanced(s)
print(res)
print(output)
print(res == output)
