class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        n = len(nums)
        res = nums[0]
        nums = [nums[i] for i in range(1, n)]
        nums.sort()
        res += nums[0] + nums[1]
        return res


nums = [1, 2, 3, 12]
output = 6

obj = Solution()
res = obj.minimumCost(nums)
print(res)
print(output)
print(res == output)
