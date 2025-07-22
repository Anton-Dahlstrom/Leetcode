class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        l, r = 0, 0
        visited = set()
        cur = 0
        while r < n:
            cur += nums[r]
            while nums[r] in visited:
                visited.remove(nums[l])
                cur -= nums[l]
                l += 1
            visited.add(nums[r])
            res = max(res, cur)
            r += 1
        return res


nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
output = 8

obj = Solution()
res = obj.maximumUniqueSubarray(nums)
print(res)
print(output)
print(res == output)
