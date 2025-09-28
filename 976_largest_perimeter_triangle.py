class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0


nums = [1, 2, 1, 10]
output = 0
obj = Solution()

res = obj.largestPerimeter(nums)
print(res)
print(output)
print(res == output)
