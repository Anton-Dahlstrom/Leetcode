class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        i = 1
        while i < len(nums):
            if nums[i] % 2 == nums[i-1] % 2:     
                return False
            i+=1
        return True

nums = [4,3,1,6]
output= False

nums = [1, 5]
output = False

obj = Solution()
res = obj.isArraySpecial(nums)
print(res)
print(output)
print(res == output)
