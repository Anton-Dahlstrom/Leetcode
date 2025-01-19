import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        dead = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        sortedHeight = [(heightMap[r][c], r, c) for c in range(
            len(heightMap[0])) for r in range(len(heightMap))]
        sortedHeight.sort(reverse=True)

        def outOfBound(r, c):
            if r < 0 or r > len(heightMap)-1 or c < 0 or c > len(heightMap[0])-1:
                return True
            return False

        def findEdges(r, c):
            for dir in directions:
                nrow, ncol = dir
                nrow += r
                ncol += c
                if outOfBound(nrow, ncol):
                    return False
                if (nrow, ncol) not in alive and (nrow, ncol) not in alivetemp and (nrow, ncol) not in edgeset:
                    heapq.heappush(edges, (heightMap[nrow][ncol], nrow, ncol))
                    edgeset.add((nrow, ncol))
            return True

        res = 0
        while sortedHeight:
            alive = set()
            height, r, c = sortedHeight.pop()
            edges = [(height, r, c)]
            edgeset = {(r, c)}
            while edges:
                tempres = 0
                height = edges[0][0]
                overflow = False
                alivetemp = set()
                while edges and edges[0][0] <= height:
                    eheight, r, c = heapq.heappop(edges)
                    if (r, c) in dead:
                        overflow = True
                        break
                    edgeset.remove((r, c))
                    if eheight < height:
                        tempres += height-eheight
                    if not findEdges(r, c) or (r, c) in dead:
                        overflow = True
                    alivetemp.add((r, c))

                if not overflow:
                    alive.update(alivetemp)
                    res += len(alive) * (edges[0][0]-height)
                    res += tempres
                else:
                    dead.update(alive)
                    break
        return res


heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
output = 4

heightMap = [[3, 3, 4, 4, 4, 2], [3, 1, 3, 2, 1, 4], [7, 3, 1, 6, 4, 1]]
output = 5

obj = Solution()
res = obj.trapRainWater(heightMap)
print(res)
print(output)
print(res == output)
