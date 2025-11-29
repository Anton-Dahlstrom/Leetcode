class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums) % k


nums = [3, 9, 7]
k = 5
output = 4

obj = Solution()
res = obj.minOperations(nums, k)
print(res)
print(output)
print(res == output)
