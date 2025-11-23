class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for i in range(num1, num2+1):
            s = str(i)
            for j in range(1, len(s)-1):
                if s[j] > s[j-1] and s[j] > s[j+1]:
                    res += 1
                elif s[j] < s[j-1] and s[j] < s[j+1]:
                    res += 1
        return res


num1 = 198
num2 = 202
output = 3

obj = Solution()
res = obj.totalWaviness(num1, num2)
print(res)
print(output)
print(res == output)
