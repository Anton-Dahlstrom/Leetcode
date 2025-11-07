class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        def canMakeMinimumPower(minpower, pfix, r, ktemp, n):
            cur = 0
            for i in range(n):
                cur += pfix[i]
                if cur < minpower:
                    diff = minpower - cur
                    cur += diff
                    ktemp -= diff
                    pfix[min(n, i+(r*2)+1)] -= diff
                    if ktemp < 0:
                        return False
            return True

        n = len(stations)
        prefix = [0]*(n+1)
        for i, station in enumerate(stations):
            start = max(0, i-r)
            end = min(n, i+r+1)
            prefix[start] += station
            prefix[end] -= station

        cur = 0
        left = float("inf")
        right = 0
        for i in range(n):
            cur += prefix[i]
            left = min(left, cur)
            right = max(right, cur)
        right += k

        while left <= right:
            mid = left+((right-left)//2)
            if not canMakeMinimumPower(mid, prefix.copy(), r, k, n):
                right = mid-1
            else:
                left = mid+1

        return left - 1


stations = [13, 12, 8, 14, 7]
r = 2
k = 23
output = 52


obj = Solution()
res = obj.maxPower(stations, r, k)
print(res)
print(output)
print(res == output)
