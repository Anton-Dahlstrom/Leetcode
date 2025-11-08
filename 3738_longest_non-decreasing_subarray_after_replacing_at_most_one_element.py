class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        intervals = []
        start = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:  # new start
                intervals.append((start, i-1))
                start = i
        if not intervals:
            return n
        if intervals[-1][1] != n-1:
            intervals.append((start, n-1))

        res = intervals[-1][-1] - intervals[-1][0] + 2
        for index, interval in enumerate(intervals[:-1]):
            start, end = interval
            size = end-start+1
            if start > 0 or end < n-1:
                size += 1
            res = max(res, size)
            nstart, nend = intervals[index+1]
            if nstart != nend and (min(nums[end-1], nums[end]) <= nums[nstart] or max(nums[end], nums[nstart]) <= nums[nstart+1]):
                res = max(res, nend-start+1)

        return min(n, res)


nums = [3, -4, -2]
output = 3

obj = Solution()
res = obj.longestSubarray(nums)
print(res)
print(output)
print(res == output)
