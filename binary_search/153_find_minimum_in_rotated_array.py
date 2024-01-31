nums = [3, 4, 5, 1, 2]
Output: 1


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid]


obj = Solution()
answer = obj.findMin(nums)
print(answer)
