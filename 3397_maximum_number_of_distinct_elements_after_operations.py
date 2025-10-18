class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        cur = float("-inf")
        for i in range(n):
            if cur < nums[i]+k:
                res += 1
                cur = max(cur+1, nums[i]-k)
        return res


nums = [1, 2, 2, 3, 3, 4]
k = 2
output = 6

obj = Solution()
res = obj.maxDistinctElements(nums, k)
print(res)
print(output)
print(res == output)
