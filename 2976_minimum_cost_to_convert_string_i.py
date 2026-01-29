from collections import defaultdict


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        edges = defaultdict(dict)
        for i in range(len(original)):
            edges[original[i]][changed[i]] = min(edges[original[i]].get(
                changed[i], float("inf")), cost[i])
        best = defaultdict(dict)

        def dfs(root, cur, val):
            if val >= best[root].get(cur, float("inf")):
                return
            best[root][cur] = val
            for key in edges[cur]:
                dfs(root, key, val + edges[cur][key])

        for i in range(97, 123):
            root = chr(i)
            for j in range(97, 123):
                start = chr(j)
                dfs(root, start, edges[root].get(start, float("inf")))

        res = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            if target[i] not in best[source[i]]:
                return -1
            res += best[source[i]][target[i]]
        return res


source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
output = 28

source = "aaaa"
target = "bbbb"
original = ["a", "c"]
changed = ["c", "b"]
cost = [1, 2]
output = 12

obj = Solution()
res = obj.minimumCost(source, target, original, changed, cost)
print(res)
print(output)
print(res == output)
