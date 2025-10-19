class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        arr = [int(s[i]) for i in range(len(s))]
        visited = set()

        def dfs(cur: list):
            best = str(cur)
            if best in visited:
                return best
            visited.add(best)
            temp1 = cur.copy()
            for i in range(1, len(temp1), 2):
                temp1[i] = (temp1[i] + a) % 10
            temp2 = cur.copy()
            split = len(temp2)-b
            temp2 = temp2[split:] + temp2[:split]
            best = min(best, dfs(temp1), dfs(temp2))
            return str(best)
        res = dfs(arr)
        res = [str(c) for c in res if c.isdigit()]
        return "".join(str(res[i])for i in range(len(res)))


s = "5525"
a = 9
b = 2
output = "2050"

obj = Solution()
res = obj.findLexSmallestString(s, a, b)
print(res)
print(output)
print(res == output)
