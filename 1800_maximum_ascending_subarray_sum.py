class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        res = nums[0]
        count = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count += nums[i]
            else:
                res = max(res, count)
                count = nums[i]

        return max(res, count)

nums = [10,20,30,5,10,50]
output = 65

obj = Solution()
res = obj.maxAscendingSum(nums)
print(res)
print(output)
print(res == output)
        