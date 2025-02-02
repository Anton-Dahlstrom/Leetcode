class Solution:
    def check(self, nums: list[int]) -> bool:
        rotated = False
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                if rotated:
                    return False
                rotated = True
        return True

nums = [3,4,5,1,2]
output= True

obj = Solution()
res = obj.check(nums)
print(res)
print(output)
print(res == output)
