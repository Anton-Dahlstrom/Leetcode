from collections import defaultdict
from math import comb


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        pairs = defaultdict(int)
        res = comb(n, 2)

        for i in range(n):
            pairs[nums[i]-i] += 1

        for cnt in pairs.values():
            if cnt > 1:
                res -= comb(cnt, 2)
        return res


nums = [4, 1, 3, 3]
output = 5


obj = Solution()
res = obj.countBadPairs(nums)
print(res)
print(output)
print(res == output)
