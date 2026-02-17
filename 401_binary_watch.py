from pyparsing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def dfs(space, val, bit):
            if bit > 10:
                return []
            res = []
            if not space:
                time = makeTime(val)
                if time:
                    res.append(time)
            else:
                res += dfs(space-1, val + (1 << bit), bit+1)
                res += dfs(space, val, bit+1)
            return res

        def makeTime(num):
            hours = num >> 6
            minutes = num % 64
            if (hours in range(0, 12) and minutes in range(0, 60)):
                minstr = str(minutes)
                if len(minstr) == 1:
                    minstr = "0" + minstr
                return str(hours) + ":" + minstr
            return ""

        return dfs(turnedOn, 0, 0)
