class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        visited = set()

        def dfs(state, pos, maxi, used):
            if pos == len(target):
                return 1
            usedtuple = tuple(used)
            if usedtuple in visited:
                return 0
            visited.add(usedtuple)
            res = 0
            for i in range(len(words)):
                start = state[i]
                for j in range(state[i], len(words[i])):
                    if target[pos] == words[i][j]:
                        state[i] = j+1
                        if j > maxi:
                            used.append((i, j))
                            res += dfs(state, pos+1, j, used)
                            used.pop()
                state[i] = start
            return res

        state = [0] * len(words)
        return dfs(state, 0, -1, []) % (1000000000 + 7)


words = ["acca", "bbbb", "caca"]
target = "aba"
output = 6

words = ["abba", "baab"]
target = "bab"
output = 4

words = ["abab", "baba", "abba", "baab"]
target = "abba"
output = 16

obj = Solution()
res = obj.numWays(words, target)
print(res)
print(output)
print(res == output)
