from typing import List


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def updateParent(node: int):
            if node == parents[node]:
                return
            updateParent(parents[node])
            parents[node] = parents[parents[node]]

        def combineSets(u,v):
            if parents[u] != parents[v]:
                if rank[parents[v]] > rank[parents[u]]:
                    u,v = v,u
                rank[parents[u]] += rank[parents[v]]
                parents[parents[v]] = parents[u]

        parents = [i for i in range(n)]
        rank = [1]*n
        res = float("inf")
        temp = []
        edgecount = 0
        for u,v,s,must in edges:
            if must:
                edgecount += 1
                res = min(res, s)
                updateParent(u)
                updateParent(v)
                combineSets(u,v)
                updateParent(u)
                updateParent(v)
            else:
                temp.append([s,u,v])
        edges = temp
        edges.sort(reverse = True)
        strengths = []
        for s,u,v in edges:
            updateParent(u)
            updateParent(v)
            if parents[u] != parents[v]:
                edgecount += 1
                combineSets(u,v)
                strengths.append(s)
                updateParent(u)
                updateParent(v)

        if edgecount != n-1:
            return -1
        for i in range(n):
            updateParent(i)
        for i in range(1,n):
            if parents[i] != parents[i-1]:
                return -1
        if strengths:
            strengths.sort()
            for i in range(min(len(strengths), k)):
                strengths[i] *= 2 
            strengths.sort()
            res = min(res, strengths[0])
        return res