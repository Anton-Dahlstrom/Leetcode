class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        temp = 1
        result = [1]*len(nums)
        for i in range(1, len(nums)):
            temp *= nums[i-1]
            result[i] *= temp
        temp = 1
        for j in reversed(range(0, len(nums)-1)):
            temp *= nums[j+1]
            result[j] *= temp
        return result


nums = [1, 2, 3, 4]
Output = [24, 12, 8, 6]

obj = Solution()
result = obj.productExceptSelf(nums)
print(result)
