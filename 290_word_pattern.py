class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hmap = {}
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        added = set()
        for i in range(len(pattern)):
            if pattern[i] not in hmap:
                if s[i] in added:
                    return False
                hmap[pattern[i]] = s[i]
                added.add(s[i])
            else:
                if hmap[pattern[i]] != s[i]:
                    return False
        return True


pattern = "abba"
s = "dog cat cat dog"
output = True

obj = Solution()
res = obj.wordPattern(pattern, s)
print(res)
print(output)
print(res == output)
