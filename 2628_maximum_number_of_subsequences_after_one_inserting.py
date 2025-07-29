class Solution:
    def numOfSubsequences(self, s: str) -> int:
        def countSubs(string):
            m = len(string)
            l, c = 0, 0
            subs = 0
            for i in range(m):
                if string[i] == "L":
                    l += 1
                elif string[i] == "C":
                    c += l
                elif string[i] == "T":
                    subs += c
            return subs

        n = len(s)
        lcount = [0] * n
        for i in range(n):
            lcount[i] = lcount[i-1]
            if s[i] == "L":
                lcount[i] += 1

        tcount = [0] * n
        for i in range(n-1, -1, -1):
            if i < n-1:
                tcount[i] = tcount[i+1]
            if s[i] == "T":
                tcount[i] += 1

        best = 0
        for i in range(0, n):
            best = max(best, lcount[i] * tcount[i])

        return max(countSubs(s) + best, countSubs("L" + s), countSubs(s + "T"))


s = "LCCT"
output = 4

obj = Solution()
res = obj.numOfSubsequences(s)
print(res)
print(output)
print(res == output)
