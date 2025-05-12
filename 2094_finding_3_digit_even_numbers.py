from typing import Counter


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        hmap = Counter(digits)
        res = []

        def dfs(cur, depth):
            if depth == 3:
                val = int("".join(cur))
                if not val % 2:
                    res.append(val)
                return
            for key in hmap:
                if depth == 0 and not key:
                    continue
                if not hmap[key]:
                    continue
                hmap[key] -= 1
                dfs(cur + [str(key)], depth+1)
                hmap[key] += 1

        dfs([], 0)
        res.sort()
        return res


digits = [2, 1, 3, 0]
output = [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]

obj = Solution()
res = obj.findEvenNumbers(digits)
print(res)
print(output)
print(res == output)
