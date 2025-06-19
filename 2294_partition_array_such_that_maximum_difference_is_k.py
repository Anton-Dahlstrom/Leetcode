class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = nums[0]
        res = 1
        for i in range(1, n):
            if nums[i] > left + k:
                res += 1
                left = nums[i]
        return res


nums = [3, 6, 1, 2, 5]
k = 2
output = 2

obj = Solution()
res = obj.partitionArray(nums, k)
print(res)
print(output)
print(res == output)
