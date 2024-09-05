class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        visited = {}

        def dfs(i1, i2):
            if (i1, i2) in visited:
                return visited[(i1, i2)]

            if i1 == len(word1) and i2 == len(word2):
                return 0

            # If no more chars in word1, return the amount of chars we need to add to finish word2
            if i1 == len(word1):
                return len(word2) - i2

            # If we made word2 return the amount of chars we need to remove from word1.
            if i2 == len(word2):
                return len(word1) - i1

            replacing = 1
            if word1[i1] == word2[i2]:
                replacing = 0

            best = min(
                1 + dfs(i1 + 1, i2),  # Delete
                replacing + dfs(i1 + 1, i2 + 1),  # Replace
                1 + dfs(i1, i2 + 1)  # Add
            )
            visited[(i1, i2)] = best
            return best

        res = dfs(0, 0)
        return res


word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"
output = 10


obj = Solution()
res = obj.minDistance(word1, word2)
print(res)
print(res == output)
