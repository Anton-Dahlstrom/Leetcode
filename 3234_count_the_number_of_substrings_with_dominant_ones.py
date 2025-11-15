class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        zeroIndexes = [i for i in range(n) if s[i] == "0"]
        zeroIndexes.append(n)
        m = len(zeroIndexes)
        kstart = 0
        for i in range(n):
            j = i
            ones = 0
            zeroes = 0
            square = 0
            while kstart < m and zeroIndexes[kstart] < i:
                kstart += 1
            k = kstart

            while j < n:
                if s[j] == "0":
                    zeroes += 1
                    square = zeroes * zeroes
                    k += 1
                else:
                    ones += 1

                if square > n:
                    break

                # if we can include all coming ones we skip forward to next zero and add them all as possible endings for our start index (i)
                if ones >= square:
                    res += zeroIndexes[k]-j
                    ones += zeroIndexes[k]-j-1
                    j = zeroIndexes[k]
                else:
                    j += 1
        return res


s = "101101"
output = 16


obj = Solution()
res = obj.numberOfSubstrings(s)
print(res)
print(output)
print(res == output)
