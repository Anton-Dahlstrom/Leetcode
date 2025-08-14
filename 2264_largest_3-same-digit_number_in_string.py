class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        res = -1
        count = 1
        for i in range(1, n):
            if num[i] == num[i-1]:
                count += 1
            else:
                count = 1
            if count == 3:
                val = int(num[i])
                if val > res:
                    res = val
        if res >= 0:
            return str(res)*3
        return ""


num = "6777133339"
output = "777"

obj = Solution()
res = obj.largestGoodInteger(num)
print(res)
print(output)
print(res == output)
