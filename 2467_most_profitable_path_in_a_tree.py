from collections import defaultdict


class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        tree = defaultdict(list)
        for e in edges:
            u, v = e
            tree[u].append(v)
            tree[v].append(u)
        bobsteps = {bob: 0}

        def bobDfs(edge, prev, steps):
            if edge == 0:
                return True
            for conn in tree[edge]:
                if conn == prev:
                    continue
                bobsteps[conn] = steps
                if bobDfs(conn, edge, steps+1):
                    return True
                bobsteps.pop(conn)
            return False
        bobDfs(bob, None, 1)

        def aliceDfs(edge, prev, curval, steps):
            if len(tree[edge]) == 1 and edge != 0:
                return curval
            res = float("-inf")
            for conn in tree[edge]:
                if conn == prev:
                    continue
                tempval = amount[conn]
                if conn in bobsteps:
                    if bobsteps[conn] < steps:
                        tempval = 0
                    elif bobsteps[conn] == steps:
                        tempval /= 2
                tempval += curval
                res = max(res, aliceDfs(conn, edge, tempval, steps+1))
            return res

        return int(aliceDfs(0, None, amount[0], 1))


edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob = 3
amount = [-2, 4, 2, -4, 6]
output = 6

obj = Solution()
res = obj.mostProfitablePath(edges, bob, amount)
print(res)
print(output)
print(res == output)
