class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        big = num
        small = 0
        if num[0] != "1":
            small = num.replace(num[0], "1")
        for i in range(len(num)):
            if big == num and num[i] != "9":
                big = num.replace(num[i], "9")
            if not small and num[i] != "0" and num[i] != num[0]:
                small = num.replace(num[i], "0")
        if not small:
            small = num
        big, small = int(big), int(small)
        return big-small


num = 123456
output = 820000


obj = Solution()
res = obj.maxDiff(num)
print(res)
print(output)
print(res == output)
