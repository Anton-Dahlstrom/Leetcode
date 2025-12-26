class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        best = 0
        res = 0
        cur = 0
        for i in range(n):
            if cur > best:
                best = cur
                res = i
            if customers[i] == "Y":
                cur += 1
            else:
                cur -= 1
        if cur > best:
            best = cur
            res = n
        return res


customers = "YYNY"
output = 2

customers

obj = Solution()
res = obj.bestClosingTime(customers)
print(res)
print(output)
print(res == output)
