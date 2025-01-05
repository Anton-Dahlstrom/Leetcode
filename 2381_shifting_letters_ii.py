import heapq
from collections import deque


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        s = [ord(c) for c in s]
        changes = [0]*len(s)
        shifts.sort(key=lambda shift: (shift[2], shift[0]))
        i = 0
        lstack = []
        rheap = []
        while shifts[i][2] == 0:
            heapq.heappush(rheap, shifts[1])
            shifts = len(rheap)
            l = shifts[0]
            i += 1
        print(shifts)
        quit()
        for shift in shifts:
            start, end, direction = shift
            if not direction:
                direction = -1
            for i in range(start, end+1):
                s[i] += direction
                if s[i] == 123:
                    s[i] = 97
                elif s[i] == 96:
                    s[i] = 122
        return "".join([chr(v) for v in s])


s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
output = "ace"

obj = Solution()
res = obj.shiftingLetters(s, shifts)
print(res)
print(output)
print(res == output)
