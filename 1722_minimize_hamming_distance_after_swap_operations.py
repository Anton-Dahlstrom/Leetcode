from typing import List


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        m = len(allowedSwaps)
        parent = [i for i in range(n)]
        rank = [0] * n

        def findparent(node):
            p = parent[node]
            if p != node:
                parent[node] = findparent(p)
            return parent[node]

        for u, v in allowedSwaps:
            if parent[u] != parent[v]:
                if rank[u] < rank[v]:
                    u, v = v, u
                vp = findparent(v)
                parent[vp] = findparent(u)

        hmap = {}
        for i, element in enumerate(source):
            p = findparent(i)
            if p not in hmap:
                hmap[p] = {element: 1}
            else:
                if element not in hmap[p]:
                    hmap[p][element] = 1
                else:
                    hmap[p][element] += 1

        score = n
        for i in range(n):
            p = parent[i]
            t = target[i]
            if t in hmap[p] and hmap[p][t] > 0:
                score -= 1
                hmap[p][t] -= 1
        return score
