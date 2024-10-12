class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if i > 0 and nums[i] == nums[i-1]:
                nums.pop(i)
                length -= 1
            else:
                i += 1
        return i


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
output = 5


obj = Solution()
res = obj.removeDuplicates(nums)
print(res)
print(output)
print(res == output)
