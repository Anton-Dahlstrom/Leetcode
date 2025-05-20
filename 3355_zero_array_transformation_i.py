class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        changes = [0] * (n+1)
        for query in queries:
            start, stop = query
            changes[start] += 1
            changes[stop+1] -= 1

        cur = 0
        for i in range(n):
            cur += changes[i]
            nums[i] -= cur
            if nums[i] > 0:
                return False

        return True


nums = [4, 3, 2, 1]
queries = [[1, 3], [0, 2]]
output = False

obj = Solution()
res = obj.isZeroArray(nums, queries)
print(res)
print(output)
print(res == output)
