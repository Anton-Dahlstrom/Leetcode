class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        visited = {}

        def dfs(i1, i2):
            if (i1, i2) in visited:
                return visited[(i1, i2)]

            if i1 == len(word1) and i2 == len(word2):
                return 0

            # If no more chars in word1, return amount of chars we need to add to finish word2
            if i1 == len(word1):
                return len(word2) - i2

            # If we made word2 return amount of chars we need to remove from word1
            if i2 == len(word2):
                return len(word1) - i1

            best = min(
                dfs(i1 + 1, i2),  # Delete
                dfs(i1 + 1, i2 + 1),  # Replace
                dfs(i1, i2 + 1)  # Add
            )

            if word1[i1] != word2[i2]:
                best += 1

            visited[(i1, i2)] = best
            if len(visited) < 20:
                print(visited)
            return best

        res = dfs(0, 0)

        print(visited[(21, 11)])
        print(visited[(20, 10)])
        print(visited[(19, 9)])
        print(visited[(18, 8)])
        print(visited[(17, 7)])
        print(visited[(16, 6)])
        print(visited[(15, 5)])
        print(visited[(14, 4)])
        print(" ")
        print(visited[(13, 3)])
        print(visited[(12, 3)])
        print(visited[(11, 3)])
        print(visited[(10, 3)])
        print(visited[(9, 3)])
        print(visited[(8, 3)])
        print(visited[(7, 3)])
        print(visited[(6, 3)])
        print(" ")
        print(visited[(5, 3)])
        print(visited[(4, 3)])
        print(" ")
        print(visited[(3, 3)])
        print(visited[(2, 3)])
        print(visited[(3, 2)])
        print(" ")
        print(visited[(2, 2)])
        print(visited[(1, 1)])
        print(visited[(4, 2)])

        return res


word1 = "horse"
word2 = "ros"
output = 3

word1 = "intention"
word2 = "execution"
output = 5

word1 = "sea"
word2 = "eat"
output = 2

# zoo g eologist
# [(0,0), (1,1), (2, 2), (5,3), (4-11, 14-21)]
word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"
output = 10

# word1 = ""
# word2 = ""
# output = 0

# word1 = ""
# word2 = "a"
# output = 1


obj = Solution()
res = obj.minDistance(word1, word2)
print(res)
print(res == output)

print(len(word1), len(word2))
