class Solution:
    def canCross(self, stones: list[int]) -> bool:
        target = stones[-1]
        stones = set(stones)

        visited = set()

        def dfs(cur, jump, target):
            if cur not in stones:
                return False
            if (cur, jump) in visited:
                return False
            else:
                visited.add((cur, jump))
            if cur == target:
                return True
            if dfs(cur+jump+1, jump+1, target):
                return True
            if jump and dfs(cur+jump, jump, target):
                return True
            if jump > 1 and dfs(cur+jump-1, jump-1, target):
                return True
            return False

        return dfs(0, 0, target)


stones = [0, 1, 3, 5, 6, 8, 12, 17]
output = True

stones = [0, 1, 2, 3, 4, 8, 9, 11]
output = False

obj = Solution()
res = obj.canCross(stones)
print(res)
print(output)
print(res == output)
