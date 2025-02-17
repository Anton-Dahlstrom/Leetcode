from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        avail = Counter(tiles)
        made = set()

        def dfs(cur, depth):
            count = 0
            if cur not in made:
                made.add(cur)
                count += 1
            if depth == len(tiles):
                return count
            for tile in avail:
                if avail[tile]:
                    avail[tile] -= 1
                    count += dfs(cur+tile, depth+1)
                    avail[tile] += 1
            return count
        return dfs("", 0) - 1


tiles = "AAABBC"
output = 188

tiles = "AAB"
output = 8

tiles = "V"
output = 1

obj = Solution()
res = obj.numTilePossibilities(tiles)
print(res)
print(output)
print(res == output)
