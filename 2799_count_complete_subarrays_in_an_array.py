from collections import defaultdict
from typing import Counter


class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        size = len(Counter(nums))
        hmap = defaultdict(int)
        unique = 0
        res = 0
        r = 0
        for i in range(n):
            while r < n and unique < size:
                if not hmap[nums[r]]:
                    unique += 1
                hmap[nums[r]] += 1
                r += 1
            if unique < size:
                break
            res += n-r+1
            hmap[nums[i]] -= 1
            if not hmap[nums[i]]:
                unique -= 1

        return res


nums = [1, 3, 1, 2, 2]
output = 4

obj = Solution()
res = obj.countCompleteSubarrays(nums)
print(res)
print(output)
print(res == output)
