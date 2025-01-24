class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        edges = {}
        for i, edgearr in enumerate(graph):
            edges[i] = set()
            for edge in edgearr:
                edges[i].add(edge)

        circular = set()

        def dfs(node):
            circle = False
            for edge in edges[node]:
                if edge in tempvisit or edge in circular:
                    circle = True
                    circular.add(node)
                    continue
                if edge in visited:
                    continue
                visited.add(edge)
                tempvisit.add(edge)
                if dfs(edge):
                    circle = True
                    circular.add(node)
                tempvisit.remove(edge)
            return circle

        visited = set()
        for edge in edges:
            if edge not in circular and edge not in visited:
                tempvisit = {edge}
                if dfs(edge):
                    circular.add(edge)

        return [i for i in range(len(graph)) if i not in circular]


graph = [[0], [2, 3, 4], [3, 4], [0, 4], []]
output = [4]

obj = Solution()
res = obj.eventualSafeNodes(graph)
print(res)
print(output)
print(res == output)
