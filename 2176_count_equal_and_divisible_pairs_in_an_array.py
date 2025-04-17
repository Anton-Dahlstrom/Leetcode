class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and not (i*j) % k:
                    res += 1
        return res


nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
output = 4

obj = Solution()
res = obj.countPairs(nums, k)
print(res)
print(output)
print(res == output)
