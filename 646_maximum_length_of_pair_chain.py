class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        cur = pairs[0][1]
        res = 1
        for pair in pairs[1:]:
            if pair[0] > cur:
                cur = pair[1]
                res += 1
        return res


pairs = [[1, 2], [2, 3], [3, 4]]
output = 2

obj = Solution()
res = obj.findlongestChain(pairs)
print(res)
print(output)
print(res == output)
