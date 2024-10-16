class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        j = 0
        for i in range(len(haystack) - len(needle) + 1):
            while haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - len(needle)
            j = 0

        return res


haystack = "mississippi"
needle = "issip"
output = 4

obj = Solution()
res = obj.strStr(haystack, needle)
print(res)
print(output)
print(res == output)
