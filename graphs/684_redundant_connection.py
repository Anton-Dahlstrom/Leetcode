class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        sets = []
        for edge in edges:
            found = False
            for i in reversed(range(len(sets))):
                print(i)
                if edge[0] in sets[i] and edge[1] in sets[i]:
                    return edge
                if edge[0] in sets[i] or edge[1] in sets[i]:
                    if not found:
                        found = sets[i]
                        found.update(set(edge))
                    else:
                        print("updating")
                        found.update(sets[i])
                        sets.pop(i)
            if not found:
                sets.append(set(edge))

        print(sets)


edges = [[1, 2], [1, 3], [2, 3]]
output = [2, 3]

obj = Solution()
res = obj.findRedundantConnection(edges)
print(res)
print(res == output)
