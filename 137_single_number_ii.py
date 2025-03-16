class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-3:
            if nums[i] == nums[i+2]:
                i += 3
            else:
                return nums[i]
        return nums[-1]


nums = [0, 1, 0, 1, 0, 1, 99]
output = 99

obj = Solution()
res = obj.singleNumber(nums)
print(res)
print(output)
print(res == output)
