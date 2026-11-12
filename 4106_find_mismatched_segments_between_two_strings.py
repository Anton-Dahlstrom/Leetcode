class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res = []
        s1temp = []
        s2temp = []
        n = len(s1)

        for i in range(n):
            if s1[i] == s2[i]:
                if s1temp:
                    res.append(["".join(s1temp), "".join(s2temp)])
                    s1temp, s2temp = [], []
            else:
                s1temp.append(s1[i])
                s2temp.append(s2[i])

        if s1temp:
            res.append(["".join(s1temp), "".join(s2temp)])
        return res