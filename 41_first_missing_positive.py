class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        hset = set() 
        for n in nums:
            hset.add(n)
        for i in range(1, len(nums)+2):
            if i not in hset:
                return i


nums = [7,8,9,11,12]
output = 1

obj = Solution()
res = obj.firstMissingPositive(nums)
print(res)
print(output)
print(res == output)