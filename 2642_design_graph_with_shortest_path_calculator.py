from collections import defaultdict
import heapq


class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.edges = defaultdict(list)
        for frm, to, cost in edges:
            self.edges[frm].append([cost, to])

    def addEdge(self, edge: list[int]) -> None:
        frm, to, cost = edge
        self.edges[frm].append([cost, to])

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        heap = self.edges[node1].copy()
        heapq.heapify(heap)
        visited = {node1}
        while heap:
            cost, node = heapq.heappop(heap)
            visited.add(node)
            if node == node2:
                return cost
            for nxt in self.edges[node]:
                if nxt[1] not in visited:
                    heapq.heappush(heap, [nxt[0]+cost, nxt[1]])
        return -1
