from collections import defaultdict


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        states = defaultdict(tuple)
        states[(0, 0)] = 0
        res = 0
        for binstr in strs:
            zeros = binstr.count("0")
            ones = len(binstr) - zeros
            temp = states.copy()
            for state in states:
                if zeros + state[0] <= m and ones + state[1] <= n:
                    newstate = (zeros + state[0], ones + state[1])
                    cnt = states[state]+1
                    if newstate in temp:
                        cnt = max(cnt, temp[newstate])
                    temp[newstate] = cnt
                    res = max(res, cnt)
            states = temp

        return res


strs = ["0", "1101", "01", "00111", "1",
        "10010", "0", "0", "00", "1", "11", "0011"]
m = 63
n = 36
output = 12


obj = Solution()
res = obj.findMaxForm(strs, m, n)
print(res)
print(output)
print(res == output)
