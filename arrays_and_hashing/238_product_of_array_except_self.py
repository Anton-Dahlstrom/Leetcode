nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

# nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1]*len(nums)
        temp = 1
        for i in range(0, len(nums)):
            temp *= nums[i]
            result[-i-1] = temp
            print(result, i)
        temp = 1
        print(result)
        for j in reversed(range(0, len(nums))):
            print(j)
            temp *= nums[j]
            result[j] *= temp
        return result


obj = Solution()
result = obj.productExceptSelf(nums)
print(result)
