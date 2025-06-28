class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        nums = [(nums[i], i) for i in range(n)]
        nums.sort()
        nums = nums[n-k:]
        nums.sort(key=lambda x:  x[1])
        nums = [nums[i][0] for i in range(k)]
        return nums


nums = [2, 1, 3, 3]
k = 2
output = [3, 3]

obj = Solution()
res = obj.maxSubsequence(nums, k)
print(res)
print(output)
print(res == output)
