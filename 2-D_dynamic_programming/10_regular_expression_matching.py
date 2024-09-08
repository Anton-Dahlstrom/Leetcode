class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True

            if j < (len(p)-1) and p[j+1] == "*":
                if p[j] == ".":
                    while i < len(s):
                        if dfs(i, j+2):
                            return True
                        i += 1
                    return dfs(i, j + 2)

                elif i < len(s) and s[i] == p[j]:
                    char = p[j]
                    if dfs(i, j + 2):
                        return True
                    i += 1
                    while i < len(s) and s[i] == char:
                        if dfs(i, j + 2):
                            return True
                        i += 1
                    return dfs(i, j + 2)

                else:
                    return dfs(i, j+2)

            # Can't advance i because there is no more pattern to use.
            if j == len(p):
                return False
            # Can't skip current pattern and move j forward because next is not "*".
            if i == len(s):
                return False

            elif p[j] == "." or s[i] == p[j]:
                return dfs(i+1, j+1)

            return False

        return dfs(0, 0)


s = "mississippi"
p = "mis*is*p*."
output = False

obj = Solution()
res = obj.isMatch(s, p)
print(res)
print(res == output)
