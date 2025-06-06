class Solution:
    def robotWithString(self, s: str) -> str:
        chars = [0]*26
        n = len(s)
        for i in range(n):
            val = ord(s[i])-97
            chars[val] += 1

        res = []
        t = []

        i = 0
        for c in range(26):
            while t and t[-1] <= c:
                res.append(t.pop())
            while chars[c] and i < n:
                val = ord(s[i])-97
                chars[val] -= 1
                if val == c:
                    res.append(val)
                else:
                    t.append(val)
                i += 1
        res += t
        return "".join([chr(i+97) for i in res])


s = "bydizfve"
output = "bdevfziy"

obj = Solution()
res = obj.robotWithString(s)
print(res)
print(output)
print(res == output)
