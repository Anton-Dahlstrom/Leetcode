class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        visited = {}
        indexes = [i for i in range(len(nums))]
        self.test = 0

        def dfs(indexArr, removed):
            # if removed in visited:
            #     return visited[removed]
            best = 0
            for i in range(1, len(indexArr)-1):
                tempIndexArr = indexArr.copy()
                tempRemoved = removed[:i] + "1" + removed[i+1:]
                val = nums[indexArr[i-1]] * \
                    nums[indexArr[i]] * nums[indexArr[i+1]]
                tempIndexArr.pop(i)
                best = max(best, val + dfs(tempIndexArr, tempRemoved))
            if removed in visited:
                print(best, visited[removed])
            visited[removed] = best
            print(visited)
            return best

        res = dfs(indexes, "0"*(len(nums)-2))
        print(visited)
        return res


nums = [3, 1, 5, 8]
output = 167

nums = [3, 1, 5]
output = 35

obj = Solution()
res = obj.maxCoins(nums)
print(res)
print(res == output)
