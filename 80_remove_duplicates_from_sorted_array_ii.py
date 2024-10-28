class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 2
        while i < len(nums):
            if nums[i] == nums[i-2]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)


nums = [1, 1, 1, 2, 2, 3]
output = 5

nums = [1, 2, 2, 2]
output = 3

obj = Solution()
res = obj.removeDuplicates(nums)
print(res)
print(output)
print(res == output)
