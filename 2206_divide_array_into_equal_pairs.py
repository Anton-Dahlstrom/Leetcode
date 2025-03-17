class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i+1]:
                return False
        return True


nums = [3, 2, 3, 2, 2, 2]
output = True

obj = Solution()
res = obj.divideArray(nums)
print(res)
print(output)
print(res == output)
