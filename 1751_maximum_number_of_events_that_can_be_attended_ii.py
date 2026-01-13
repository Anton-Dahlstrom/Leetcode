class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])

        def bs(arr, val):
            l, r = 0, len(arr)-1
            while l <= r:
                mid = l+((r-l)//2)
                if arr[mid][0] < val:
                    l = mid+1
                else:
                    r = mid-1
            return l-1

        # end, val
        dp = [[(0, 0)] for _ in range(k)]
        res = 0
        for start, end, val in events:
            for i in range(k):
                tempval = val
                if i and start > dp[i-1][0][0]:
                    index = bs(dp[i-1], start)
                    tempval += dp[i-1][index][1]
                if tempval > dp[i][-1][1]:
                    dp[i].append((end, tempval))
                res = max(res, tempval)

        return res


events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
k = 2
output = 7

obj = Solution()
res = obj.maxValue(events, k)
print(res)
print(output)
print(res == output)
