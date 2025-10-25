class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        cur = 0
        temp = 0
        for i in range(1, n+1):
            cur += 1
            res += cur
            if not i % 7:
                temp += cur
                cur -= 6
        return res


n = 10
output = 37

obj = Solution()
res = obj.totalMoney(n)
print(res)
print(output)
print(res == output)
