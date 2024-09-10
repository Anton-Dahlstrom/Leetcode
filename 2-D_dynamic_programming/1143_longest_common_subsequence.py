class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        set1 = set(text1)
        common_chars = set1.intersection(text2)
        text1 = "".join(char for char in text1 if char in common_chars)
        text2 = "".join(char for char in text2 if char in common_chars)
        if not text1 or not text2:
            return 0

        visited = {}

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in visited:
                return visited[(i, j)]

            adding = 0
            if text1[i] == text2[j]:
                adding = 1

            res = max(
                dfs(i+1, j),
                dfs(i, j+1),
                adding + dfs(i+1, j+1)
            )
            visited[(i, j)] = res
            return res

        return dfs(0, 0)


text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"
output = 3


obj = Solution()
res = obj.longestCommonSubsequence(text1, text2)
print(res)
print(res == output)
