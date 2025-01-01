class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        if s[0] == "0":
            score += 1
        if s[-1] == "1":
            score += 1

        for i in range(1, len(s)-1):
            if s[i] == "1":
                score += 1

        res = score
        for i in range(1, len(s)-1):
            if s[i] == "1":
                score -= 1
            elif s[i] == "0":
                score += 1
            res = max(res, score)
        return res


s = "1011011"
output = 5

obj = Solution()
res = obj.maxScore(s)
print(res)
print(output)
print(res == output)
