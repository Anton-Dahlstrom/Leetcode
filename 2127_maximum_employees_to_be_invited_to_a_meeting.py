class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        n = len(favorite)
        pairs = {}
        circle = set()
        best = {}
        self.maxloop = 0

        def dfs(node):
            if node in best:
                print(best)
                return best[node][0]+1, False, best[node][1]
            if node in pairs:
                return 1, False, node
            if favorite[favorite[node]] == node:
                pairs[node] = 0
                pairs[favorite[node]] = 0
                return 1, False, node

            if node in circle:
                return 0, True, -1
            if node in visited:
                return 1, True, node
            visited.add(node)

            child = favorite[node]
            size, loop, loopnode = dfs(child)

            if loop and loopnode == node:
                self.maxloop = max(size, self.maxloop)
                return size, True, -1

            if not loop:
                pairs[loopnode] = max(pairs[loopnode], size)
                best[node] = (size, loopnode)

            return size+1, loop, loopnode

        for i in range(n):
            visited = set()
            size, loop, pair = dfs(i)
            if loop:
                circle.update(visited)

        pairtotal = 0
        for key in pairs:
            pairtotal += pairs[key]+1
        return max(self.maxloop, pairtotal)


favorite = [4, 3, 1, 5, 1, 3]
output = 5


obj = Solution()
res = obj.maximumInvitations(favorite)
print(res)
print(output)
print(res == output)
