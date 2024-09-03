class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        cur = n
        while True:
            if cur == 1:
                return True
            if cur in visited:
                return False
            visited.add(cur)
            s = str(cur)
            temp = 0
            for char in s:
                integer = int(char)
                temp += integer * integer
            cur = temp


n = 19
output = True

obj = Solution()
res = obj.isHappy(n)
print(res)
print(res == output)
