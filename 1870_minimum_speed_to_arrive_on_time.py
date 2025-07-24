import math


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        n = len(dist)

        def arriveInTime(speed):
            time = 0
            for i in range(n):
                time = (dist[i]/speed) + time
                if time > hour:
                    return False
                time = math.ceil(time)
            return True

        if not arriveInTime(10**7):
            return -1

        l, r = 1, 10**7

        while l < r:
            mid = l + ((r-l)//2)
            if not arriveInTime(mid):
                l = mid + 1
            else:
                r = mid
        return l


dist = [1, 3, 2]
hour = 6
output = 1

# dist = [1, 3, 2]
# hour = 2.7
# output = 3

dist = [1, 1]
hour = 1.0
output = -1

obj = Solution()
res = obj.minSpeedOnTime(dist, hour)
print(res)
print(output)
print(res == output)
