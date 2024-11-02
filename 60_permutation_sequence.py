class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.tries = 0

        def search(val, used, count, n):
            if count == n:
                self.tries += 1
                if self.tries == k:
                    return val

            for i in range(1, n+1):
                if i in used:
                    continue
                temp = val + (i * (10 ** (n - count - 1)))
                used.add(i)
                res = search(temp, used, count+1, n)
                if res:
                    return res
                used.remove(i)

        return str(search(0, set(), 0, n))


n = 3
k = 3
output = "213"


obj = Solution()
res = obj.getPermutation(n, k)
print(res)
print(output)
print(res == output)
