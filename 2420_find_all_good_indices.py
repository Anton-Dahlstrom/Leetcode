class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        # Keeps track of how far a subarray will continue to increase/decrease
        increasing = [0] * n
        decreasing = [0] * n
        decreasing[-1] = n-1
        prev = 0
        # Populate increasing array front to back.
        for i in range(1, n-k):
            if nums[i] > nums[i-1]:
                prev = i
            increasing[i] = prev
        prev = n-1
        # Populate decreasing array backwards.
        for i in range(n-2, k-1, -1):
            if nums[i] > nums[i+1]:
                prev = i
            decreasing[i] = prev

        res = []
        # Look through all indexes to see if they're valid.
        for i in range(k, n-k):
            if increasing[i-1] <= i-k and decreasing[i+1] >= i+k:
                res.append(i)
        return res


nums = [2, 1, 1, 1, 3, 4, 1]
k = 2
output = [2, 3]

obj = Solution()
res = obj.goodIndices(nums, k)
print(res)
print(output)
print(res == output)
