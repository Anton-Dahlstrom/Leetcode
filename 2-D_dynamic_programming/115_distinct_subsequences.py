class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        visited = {}

        def dfs(sindex, tindex):

            if (sindex, tindex) in visited:
                return visited[(sindex, tindex)]
            if tindex == len(t):
                return 1

            total = 0
            for i in range(sindex, len(s)):
                if len(s)-i < len(t) - tindex:
                    break
                if s[i] == t[tindex]:
                    total += dfs(i+1, tindex + 1)

            visited[(sindex, tindex)] = total
            return total

        return dfs(0, 0)


s = "rabbbit"
t = "rabbit"
output = 3

s = "adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc"
t = "bcddceeeebecbc"
output = 700531452

obj = Solution()
res = obj.numDistinct(s, t)
print(res)
print(res == output)
