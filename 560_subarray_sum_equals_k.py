from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i-1]
        visited = defaultdict(int)
        res = 0
        for val in prefix:
            needToRemove = val - k
            if needToRemove == 0:
                res += 1
            if needToRemove in visited:
                res += visited[needToRemove]
            visited[val] += 1
        return res


nums = [1, 2, 3]
k = 3
output = 2


obj = Solution()
res = obj.subarraySum(nums, k)
print(res)
print(output)
print(res == output)
