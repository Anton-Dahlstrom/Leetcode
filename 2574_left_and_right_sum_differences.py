from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = sum(nums)
        left = 0
        res = [0] * n
        for i in range(n):
            right -= nums[i]
            res[i] = abs(left-right)
            left += nums[i]
        return res
