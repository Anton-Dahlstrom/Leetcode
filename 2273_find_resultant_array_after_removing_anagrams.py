class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        n = len(words)
        arr = [0]*n
        for i in range(n):
            w = list(words[i])
            w.sort()
            w = "".join(w)
            arr[i] = w
        res = [words[0]]
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                continue
            res.append(words[i])
        return res


words = ["abba", "baba", "bbaa", "cd", "cd"]
output = ["abba", "cd"]

obj = Solution()
res = obj.removeAnagrams(words)
print(res)
print(output)
print(res == output)
