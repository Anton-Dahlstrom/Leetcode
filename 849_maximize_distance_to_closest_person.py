class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        prev = -1
        res = 0
        for i in range(n):
            if seats[i] == 1:
                if prev < 0:
                    res = i
                else:
                    res = max(res, (i-prev)//2)
                prev = i
        res = max(res, n-prev-1)
        return res


seats = [1, 0, 0, 0, 1, 0, 1]
output = 2


obj = Solution()
res = obj.maxDistToClosest(seats)
print(res)
print(output)
print(res == output)
