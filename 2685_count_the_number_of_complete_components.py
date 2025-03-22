class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[]for i in range(n)]
        rank = [1] * n
        parent = [i for i in range(n)]
        for edge in edges:
            v1, v2 = edge
            # Add connection in graph
            graph[v1].append(v2)
            graph[v2].append(v1)

            # Lazy updating of parents
            while parent[v1] != parent[parent[v1]]:
                parent[v1] = parent[parent[v1]]
            while parent[v2] != parent[parent[v2]]:
                parent[v2] = parent[parent[v2]]

            # Check if sets are disjoint and join on larger set if they are.
            if parent[v1] != parent[v2]:
                # Ensure v1 has greater rank to reduce redundant code.
                if rank[parent[v1]] < rank[parent[v2]]:
                    v1, v2 = v2, v1
                # Update rank and merge sets
                rank[parent[v1]] += rank[parent[v2]]
                parent[parent[v2]] = parent[parent[v1]]
                parent[v2] = parent[v1]

        complete = set()
        incomplete = set()
        # Search for any node with less connections than the rank of its parent.
        # Store those parents as incomplete and the rest as complete.
        for node in range(n):
            while parent[node] != parent[parent[node]]:
                parent[node] = parent[parent[node]]
            if parent[node] in incomplete:
                continue
            if len(graph[node])+1 < rank[parent[node]]:
                if parent[node] in complete:
                    complete.remove(parent[node])
                incomplete.add(parent[node])
            else:
                complete.add(parent[node])
        # Return the amount of complete sets.
        return len(complete)


n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
output = 3

n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
output = 1

n = 5
edges = [[1, 2], [3, 4], [1, 4], [2, 3], [1, 3], [2, 4]]
output = 2

obj = Solution()
res = obj.countCompleteComponents(n, edges)
print(res)
print(output)
print(res == output)
