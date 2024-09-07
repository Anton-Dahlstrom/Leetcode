class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Need to account for * allowing the previous character to not be matched.

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True

            if i == len(s) or j == len(p):
                return False

            if p[j] == "*":

                if p[j-1] == "." or s[i] == p[j-1]:
                    if dfs(i+1, j):
                        return True
                    return dfs(i+1, j+1)
                else:
                    return dfs(i, j+1)

            if p[j] == ".":
                return dfs(i+1, j+1)

            elif p[j] == s[i]:
                return dfs(i+1, j+1)

            return dfs(i, j+1)

        return dfs(0, 0)


# s = "aa"
# p = "a*"
# output = True

# s = "aa"
# p = "a"
# output = False

# s = "aab"
# p = "c*a*b"
# output = True

# s = "ab"
# p = ".*c"
# output = False

s = "aaa"
p = "ab*a*c*a"
output = True

obj = Solution()
res = obj.isMatch(s, p)
print(res)
print(res == output)
