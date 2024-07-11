from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res


nums = [4, 1, 2, 1, 2]
output = 4

obj = Solution()
res = obj.singleNumber(nums)
print(res)
print(res == output)
