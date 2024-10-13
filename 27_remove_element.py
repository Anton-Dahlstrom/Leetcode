class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


nums = [3, 2, 2, 3]
val = 3
output = 2


obj = Solution()
res = obj.removeElement(nums, val)
print(output)
print(res)
print(res == output)
