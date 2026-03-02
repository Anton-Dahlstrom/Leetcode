class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        found = True
        while found:
            first = {}
            found = False
            for i in range(len(s)):
                if s[i] in first and i <= first[s[i]] + k:
                    s = s[:i] + s[i+1:]
                    found = True
                    break
                first[s[i]] = i
        return s


s = "aabca"
k = 2
output = "abca"

obj = Solution()
res = obj.mergeCharacters(s, k)
print(res)
print(output)
print(res == output)
