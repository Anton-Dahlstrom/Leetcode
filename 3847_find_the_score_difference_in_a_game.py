from ast import List


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        active = True
        p1 = 0
        p2 = 0
        for i in range(len(nums)):
            if (i+1) % 6 == 0:
                active = active == False
            if nums[i] % 2 == 1:
                active = active == False
            if active:
                p1 += nums[i]
            else:
                p2 += nums[i]
        return p1 - p2
