class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] = 1
            else:
                nums[i] = 0

        nums.sort()
        return nums


nums = [1, 5, 1, 4, 2]
output = [0, 0, 1, 1, 1]

obj = Solution()
res = obj.transformArray(nums)
print(res)
print(output)
print(res == output)
