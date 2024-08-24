class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]

        def dfs(arr):
            best = 0
            for i in range(1, len(arr)-1):
                temp = arr.copy()
                val = arr[i-1] * arr[i] * arr[i+1]
                temp.pop(i)
                best = max(best, val + dfs(temp))
            return best
        return dfs(nums)


nums = [3, 1, 5, 8]
output = 167

obj = Solution()
res = obj.maxCoins(nums)
print(res)
print(res == output)
