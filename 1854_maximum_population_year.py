class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        arr = [0] * 101
        base = 1950
        for log in logs:
            birth, death = log
            arr[birth-base] += 1
            arr[death-base] -= 1
        res = -1
        biggest = -1
        cur = 0
        for i in range(len(arr)):
            cur += arr[i]
            if cur > biggest:
                res = i
                biggest = cur
        return res + base


logs = [[1993, 1999], [2000, 2010]]
output = 1993

obj = Solution()
res = obj.maximumPopulation(logs)
print(res)
print(output)
print(res == output)
