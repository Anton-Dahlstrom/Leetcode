class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] < k:
                res += 1
        return res


nums = [2, 11, 10, 1, 3]
k = 10
output = 3

obj = Solution()
res = obj.minOperations(nums, k)
print(res)
print(output)
print(res == output)
