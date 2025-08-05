class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        count = [0]*n
        prevCandle = [-1]*n
        nextCandle = [-1]*n
        for i in range(n):
            count[i] = count[i-1]
            if s[i] == "|":
                count[i] += 1

        prev = -1
        for i in range(n):
            if s[i] == "|":
                prev = i
            if prev >= 0:
                prevCandle[i] = prev

        nxt = -1
        for i in range(n-1, -1, -1):
            if s[i] == "|":
                nxt = i
            if nxt >= 0:
                nextCandle[i] = nxt
        res = []
        for l, r in queries:
            lc = nextCandle[l]
            rc = prevCandle[r]
            cnt = count[r]
            if lc < 0 or rc < 0:
                res.append(0)
                continue
            if l:
                cnt -= count[l-1]
            ans = max(0, rc-lc+1-cnt)
            res.append(ans)
        return res


s = "**|**|***|"
queries = [[2, 5], [5, 9]]
output = [2, 3]


obj = Solution()
res = obj.platesBetweenCandles(s, queries)
print(res)
print(output)
print(res == output)
