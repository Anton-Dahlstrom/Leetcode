class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        mini, maxi = min(nums), max(nums)
        nums = set(nums)
        res = []
        for i in range(mini+1, maxi):
            if i not in nums:
                res.append(i)
        return res


nums = [1, 4, 2, 5]
output = [3]

obj = Solution()
res = obj.findMissingElements(nums)
print(res)
print(output)
print(res == output)
