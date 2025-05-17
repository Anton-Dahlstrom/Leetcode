class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        zeros, ones = 0, 0
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1

        for i in range(n):
            if zeros:
                nums[i] = 0
                zeros -= 1
            elif ones:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2


nums = [2, 0, 2, 1, 1, 0]
output = [0, 0, 1, 1, 2, 2]

obj = Solution()
res = obj.sortColors(nums)
print(nums)
print(output)
print(nums == output)
