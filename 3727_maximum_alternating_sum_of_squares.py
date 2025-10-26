class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = [num**2 for num in nums]
        nums.sort()
        n = len(nums)
        mid = n//2
        res = 0
        for i in range(mid):
            res += nums[i+mid]
            res -= nums[i]
        if n % 2:
            res += nums[-1]
        return res


nums = [1, -1, 2, -2, 3, -3]
output = 16

obj = Solution()
res = obj.maxAlternatingSum(nums)
print(res)
print(output)
print(res == output)
