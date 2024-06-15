from typing import List

nums = [2, 3, 1, 1, 4]
Output: 2


class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = nums[0]
        jumps = 0
        start = 0
        index = 0
        while start < len(nums)-1:
            jumps += 1
            tempindex = index
            tempreach = reach + start
            for i in range(1, reach+1):
                if start + i == len(nums)-1:
                    return jumps
                index = start + i

                if nums[index] + index >= tempreach:
                    tempreach = nums[index] + index
                    tempindex = index

            start = start + reach
            reach = (tempindex + nums[tempindex]) - start
        return jumps


obj = Solution()
result = obj.jump(nums)
print(result)
