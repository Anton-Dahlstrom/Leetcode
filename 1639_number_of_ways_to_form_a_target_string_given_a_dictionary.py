class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        arr = [[0 for _ in range(len(words[0]))] for _ in range(len(target))]
        diff = len(words[0]) - len(target)
        for i in range(len(arr)):
            for j in range(i, i + diff + 1):
                for word in words:
                    if word[j] == target[i]:
                        arr[i][j] += 1
        for i in range(len(arr)-1):
            temp = [0] * len(words[0])
            for j in range(i, i + diff + 1):
                for k in range(j+1, i+diff+2):
                    temp[k] += arr[i][j] * arr[i+1][k]
            arr[i+1] = temp
        return sum(arr[-1]) % (1000000000+7)


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
