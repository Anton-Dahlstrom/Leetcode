class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zeroes = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zeroes += 1
            else:
                i += 1
        nums += [0]*zeroes


nums = [0, 1, 0, 3, 12]
output = [1, 3, 12, 0, 0]


obj = Solution()
res = obj.moveZeroes(nums)
print(res)
print(output)
print(res == output)
