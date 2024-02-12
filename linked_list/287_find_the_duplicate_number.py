nums = [1, 3, 4, 2, 2]
Output: 2


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hmap = {}
        for num in nums:
            if num in hmap:
                return num
            hmap[num] = 1


obj = Solution()
result = obj.findDuplicate(nums)
print(result)
