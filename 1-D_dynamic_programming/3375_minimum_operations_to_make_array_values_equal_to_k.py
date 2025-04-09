class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        used = set()
        for i in range(len(nums)):
            if nums[i] < k:
                return -1
            elif nums[i] > k and nums[i] not in used:
                used.add(nums[i])
        return len(used)


nums = [5, 2, 5, 4, 5]
k = 2
output = 2

obj = Solution()
res = obj.minOperations(nums, k)
print(res)
print(output)
print(res == output)
