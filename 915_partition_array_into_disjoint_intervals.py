class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        n = len(nums)
        prefixmin = [0] * n
        prefixmax = [0] * n
        cur = nums[-1]
        for i in range(n-1, -1, -1):
            cur = min(cur, nums[i])
            prefixmin[i] = cur
        cur = -1
        for i in range(n):
            cur = max(cur, nums[i])
            prefixmax[i] = cur
        for i in range(n-1):
            if prefixmax[i] <= prefixmin[i+1]:
                return i+1


nums = [5, 0, 3, 8, 6]
output = 3

obj = Solution()
res = obj.partitionDisjoint(nums)
print(res)
print(output)
print(res == output)
