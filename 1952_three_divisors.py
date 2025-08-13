class Solution:
    def isThree(self, n: int) -> bool:
        res = False
        for i in range(2, n):
            if not n % i:
                if res:
                    return False
                res = True
        return res


n = 4
output = True


obj = Solution()
res = obj.isThree(n)
print(res)
print(output)
print(res == output)
