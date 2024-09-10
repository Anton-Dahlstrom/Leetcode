class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        visited = {}
        indexes = [i for i in range(len(nums))]

        def dfs(indexArr, removed):
            if removed in visited:
                return visited[removed]
            best = 0

            for i in range(1, len(indexArr)-1):
                tempIndexArr = indexArr.copy()
                val = nums[indexArr[i-1]] * \
                    nums[indexArr[i]] * nums[indexArr[i+1]]

                tempIndexArr.pop(i)
                tempRemoved = tuple(tempIndexArr)
                best = max(best, val + dfs(tempIndexArr, tempRemoved))
            visited[removed] = best
            return best

        res = dfs(indexes, ())
        return res


nums = [3, 1, 5, 8]
output = 167

nums = [3, 1, 5]
output = 35

nums = [1, 6, 8, 3, 4, 6, 4, 7, 9, 8, 0, 6, 2, 8]
output = 3376

nums = [8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2]
output = 3394

obj = Solution()
res = obj.maxCoins(nums)
print(res)
print(res == output)
