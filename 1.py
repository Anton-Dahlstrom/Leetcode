class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        big = num
        small = 0
        for i in range(len(num)):
            if big == num and num[i] != "9":
                big = num.replace(num[i], "9")
            if not small and num[i] != "0":
                small = num.replace(num[i], "0")
        return int(big) - int(small)


num = 11891
output = 99009


obj = Solution()
res = obj.minMaxDifference(num)
print(res)
print(output)
print(res == output)
