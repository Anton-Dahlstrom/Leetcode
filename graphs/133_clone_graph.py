from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        stack = [node]
        hmap = {}
        while stack:
            old = stack.pop()
            if old.val not in hmap:
                hmap[old.val] = Node(old.val)
            new = hmap[old.val]
            added = set([n.val for n in new.neighbors])
            for oldNeighbor in old.neighbors:
                if oldNeighbor.val not in hmap:
                    hmap[oldNeighbor.val] = Node(oldNeighbor.val)
                    stack.append(oldNeighbor)
                if oldNeighbor.val not in added:
                    new.neighbors.append(hmap[oldNeighbor.val])
                    hmap[oldNeighbor.val].neighbors.append(hmap[new.val])
                    added.add(oldNeighbor.val)
        return hmap[node.val]


adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
output = [[2, 4], [1, 3], [2, 4], [1, 3]]

obj = Solution()
res = obj.maxAreaOfIsland(adjList)
print(res)
print(res == output)
