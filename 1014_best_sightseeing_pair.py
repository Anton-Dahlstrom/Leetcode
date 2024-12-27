class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        l = 0
        res = 0
        while l < len(values)-1:
            r = l + 1
            while r < len(values):
                res = max(res, values[l] + values[r] - (r-l))
                if values[r] + (r-l) > values[l]:
                    l = r-1
                    break
                r += 1
            l += 1
        return res


values = [8, 1, 5, 2, 6]
output = 11

obj = Solution()
res = obj.maxScoreSightseeingPair(values)
print(res)
print(output)
print(res == output)
