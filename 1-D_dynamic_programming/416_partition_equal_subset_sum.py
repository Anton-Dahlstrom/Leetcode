from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        diff = set()
        diff.add(nums[0])
        for val in nums[1:]:
            temp = set()
            for dif in diff:
                temp.add(dif+val)
                temp.add(dif-val)
            diff = temp
        if 0 in diff:
            return True
        return False


nums = [1, 5, 11, 5]
output = True

nums = [3, 4, 5, 100, 102]
output = True

obj = Solution()
res = obj.canPartition(nums)
print(res)
print(res == output)
