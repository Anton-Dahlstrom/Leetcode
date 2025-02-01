class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        def dfs(cur, n):
            for i in range(0,10):
                if not (cur + i):
                    continue
                if cur + i <= n:
                    res.append(cur+i)
                    dfs((cur+i)*10, n)
                else:
                    return

        dfs(0,n)

        return res

n = 13
output= [1,10,11,12,13,2,3,4,5,6,7,8,9]

obj = Solution()
res = obj.lexicalOrder(n)
print(res)
print(output)
print(res == output)
