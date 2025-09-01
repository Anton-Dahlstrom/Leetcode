class Solution:
    def minDifference(self, n: int, k: int) -> list[int]:
        self.min = float("inf")
        self.temp = []
        self.final = []
        self.divs = [1]

        for i in range(2, n+1):
            if not n % i:
                self.divs.append(i)

        def dfs(j, cur, steps):
            if steps == k:
                if cur == n:
                    diff = self.temp[-1]-self.temp[0]
                    print(diff)
                    if diff < self.min:
                        self.min = diff
                        self.final = self.temp.copy()
                return
            for i in range(j, len(self.divs)):
                if cur * self.divs[i] > n:
                    break
                self.temp.append(self.divs[i])
                dfs(i, cur*self.divs[i], steps+1)
                self.temp.pop()

        for i in range(len(self.divs)):
            self.temp.append(self.divs[i])
            dfs(i, self.divs[i], 1)
            self.temp.pop()
        return self.final


n = 44
k = 3
output = [2, 2, 11]

obj = Solution()
res = obj.minDifference(n, k)
print(res)
print(output)
print(res == output)
