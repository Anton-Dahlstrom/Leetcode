class Solution:
    def findScore(self, nums: list[int]) -> int:
        score = 0
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()
        marked = set()
        for num in nums:
            val, index = num
            if index in marked:
                continue
            score += val
            marked.add(index)
            if index > 0:
                marked.add(index-1)
            if index < len(nums)-1:
                marked.add(index+1)
            if len(marked) == len(nums):
                return score
        return score


nums = [2, 1, 3, 4, 5, 2]
output = 7

obj = Solution()
res = obj.findScore(nums)
print(res)
print(output)
print(res == output)
