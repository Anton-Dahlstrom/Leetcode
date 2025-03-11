class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = {}
        n = len(s)
        l = 0
        r = 0
        res = 0

        while r <= n:
            if len(counter) < 3:
                if not r < n:
                    break
                cur = s[r]
                if cur in counter:
                    counter[cur] += 1
                else:
                    counter[cur] = 1
                r += 1
            else:
                res += n - r + 1
                cur = s[l]
                counter[cur] -= 1
                if not counter[cur]:
                    counter.pop(cur)
                l += 1

        return res


s = "abcabc"
output = 10


obj = Solution()
res = obj.numberOfSubstrings(s)
print(res)
print(output)
print(res == output)
