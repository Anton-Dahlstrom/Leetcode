class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = max(abs(nums[i] - nums[i-1]), res)
        return res


nums = [1, 2, 4]
output = 3
nums = [-5, -10, -5]
output = 5
obj = Solution()
res = obj.maxAdjacentDistance(nums)
print(res)
print(output)
print(res == output)
