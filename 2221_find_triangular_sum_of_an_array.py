class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        while n > 1:
            temp = [0]*(n-1)
            for i in range(n-1):
                temp[i] = (nums[i] + nums[i+1]) % 10
            nums = temp
            n = len(nums)
        return nums[0]


nums = [1, 2, 3, 4, 5]
output = 8

obj = Solution()
res = obj.triangularSum(nums)
print(res)
print(output)
print(res == output)
