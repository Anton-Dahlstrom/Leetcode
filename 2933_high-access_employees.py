from collections import deque


class Solution:
    def findHighAccessEmployees(self, access_times: list[list[str]]) -> list[str]:
        access_times.sort()
        n = len(access_times)
        cur = -1
        times = deque()
        res = []
        skip = None
        for i in range(n):
            emp, time = access_times[i]
            time = int(time)
            if emp == skip:
                continue
            if emp != cur:
                cur = emp
                times = deque()
            elif len(times) >= 2:
                if times[-1] + 100 > time:
                    res.append(emp)
                    skip = emp
                times.pop()
            times.appendleft(time)
        return res


access_times = [["qzgyyji", "1945"], ["qzgyyji", "1855"], ["jsxkxtugi", "1859"], ["hhjuaxal", "1940"], ["hhjuaxal",
                                                                                                        "1831"], ["jsxkxtugi", "1841"], ["hhjuaxal", "1918"], ["jsxkxtugi", "1941"], ["hhjuaxal", "1852"]]
output = ["hhjuaxal"]


obj = Solution()
res = obj.findHighAccessEmployees(access_times)
print(res)
print(output)
print(res == output)
