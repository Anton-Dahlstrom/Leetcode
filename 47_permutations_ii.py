class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(arr, cur):
            next = set()
            if not arr:
                res.append(cur)
                return 
            for i, v in enumerate(arr):
                if v in next:
                    continue
                next.add(v)
                tempArr = arr.copy()
                v = tempArr.pop(i)
                tempCur = cur.copy()
                tempCur.append(v)
                dfs(tempArr, tempCur)
        dfs(nums, [])
        return res 



nums = [1,1,2]
output = [[1,1,2],
          [1,2,1],
          [2,1,1]]


obj = Solution()
res = obj.permuteUnique(nums)
print(res)
print(output)
print(res == output)