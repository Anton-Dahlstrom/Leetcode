class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        arr = [0]*n
        cur = float("inf")
        for i in range(n-1, -1, -1):
            cur = min(cur, nums[i])
            arr[i] = cur
        cur = float("-inf")
        for i in range(n):
            cur = max(cur, nums[i])
            score = cur-arr[i]
            if score <= k:
                return i
        return -1
