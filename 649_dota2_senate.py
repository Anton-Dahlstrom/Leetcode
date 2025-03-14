class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = []
        r = []
        for i in range(len(senate)):
            char = senate[i]
            if char == "D":
                d.append(i)
            else:
                r.append(i)
        di = ri = 0
        while d and r:
            if di >= len(d) and ri >= len(r):
                di = ri = 0
                continue
            if di >= len(d):
                d = d[1:]
                ri += 1
                continue
            if ri >= len(r):
                r = r[1:]
                di += 1
                continue

            if d[di] < r[ri]:
                r.pop(ri)
                di += 1
            else:
                d.pop(di)
                ri += 1

        if d:
            return "Dire"
        return "Radiant"


senate = "RRDDD"
output = "Radiant"

obj = Solution()
res = obj.predictPartyVictory(senate)
print(res)
print(output)
print(res == output)
