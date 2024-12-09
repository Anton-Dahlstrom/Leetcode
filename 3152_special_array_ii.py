class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        res = []
        breakpoints = []
        for i in range(len(nums)-1):
            if (nums[i] % 2 + nums[i+1] % 2) != 1:
                breakpoints.append((i))
        breakpoints.append(len(nums))
        arr = [0]*len(nums)
        j = 0
        i = 0
        while i < len(nums):
            if i > breakpoints[j]:
                j += 1
            arr[i] = breakpoints[j]
            i += 1

        for query in queries:
            start, stop = query
            if arr[start] < stop:
                res.append(False)
            else:
                res.append(True)
        return res


nums = [4, 3, 1, 6]
queries = [[0, 2], [2, 3]]
output = [False, True]

obj = Solution()
res = obj.isArraySpecial(nums, queries)
print(res)
print(output)
print(res == output)
