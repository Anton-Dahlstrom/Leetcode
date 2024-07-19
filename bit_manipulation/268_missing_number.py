class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        increase = 1
        res = 0
        for num in nums:
            res += increase - num
            increase += 1
        return res


nums = [3, 0, 1]
output = 2

obj = Solution()
res = obj.missingNumber(nums)
print(res)
print(res == output)
