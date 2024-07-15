class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights:
            return None
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        lenR = len(heights)
        lenC = len(heights[0])
        visited = set()
        results = set()

        def dfs(coord):
            r, c = coord
            finalRes = [r == 0 or c == 0, r == lenR-1 or c == lenC-1]
            for d in directions:
                newR, newC = r + d[0], c + d[1]
                if ((-1 < newR < lenR) and
                    (-1 < newC < lenC) and
                    (newR, newC) not in visited and
                        (heights[r][c] >= heights[newR][newC])):
                    if (newR, newC) in results:
                        return [True, True]

                    visited.add((newR, newC))
                    res = dfs((newR, newC))
                    if res[0] and res[1]:
                        finalRes = [True, True]
                    elif res[0]:
                        finalRes[0] = True
                    elif res[1]:
                        finalRes[1] = True
                    if finalRes[0] and finalRes[1]:
                        results.add((r, c))
                        return finalRes
            return finalRes

        for r in range(lenR):
            for c in range(lenC):
                if (r, c) in results:
                    continue
                visited = set()
                search = dfs((r, c))
                if search == [True, True]:
                    results.add((r, c))
        return list(results)


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]].sort()

obj = Solution()
res = obj.pacificAtlantic(heights)
print(res)
print(res.sort() == output)
