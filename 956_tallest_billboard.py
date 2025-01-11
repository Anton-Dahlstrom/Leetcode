class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        self.maxval = sum(rods)
        self.res = 0
        self.count = 0
        visited = set()

        def dfs(arr, i, left, right, possible):
            state = (i, left, right)
            if left > possible/2 or right > possible/2 or state in visited or possible <= self.res*2:
                return
            visited.add(state)
            if i == len(arr):
                self.count += 1
                if left == right:
                    if left*2 == self.maxval:
                        self.solved = True
                    self.res = max(self.res, left)
                return

            if left > right:
                dfs(arr, i+1, left, right+arr[i], possible)
                dfs(arr, i+1, left+arr[i], right, possible)
            else:
                dfs(arr, i+1, left+arr[i], right, possible)
                dfs(arr, i+1, left, right+arr[i], possible)
            dfs(arr, i+1, left, right, possible-arr[i])
        dfs(rods, 0, 0, 0, self.maxval)

        return self.res


rods = [96, 112, 101, 100, 104, 93, 106, 99, 114, 81, 94]
output = 503


obj = Solution()
res = obj.tallestBillboard(rods)
print(res)
print(output)
print(res == output)
