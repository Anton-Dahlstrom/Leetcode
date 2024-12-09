class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        # Need to find areas of array that are "unsafe" ahead of time.
        res = []
        for query in queries:
            start, stop = query

            i = start
            while i < stop:
                print(nums[i] % 2, nums[i+1] % 2)
                if (nums[i] % 2 + nums[i+1] % 2) != 1:
                    res.append(False)
                    break
                i += 1
            if i == stop:
                res.append(True)

        return res


nums = [4, 3, 1, 6]
queries = [[0, 2], [2, 3]]
output = [False, True]

# nums = [2, 1]
# queries = [[0, 1]]
# output = [True]

obj = Solution()
res = obj.isArraySpecial(nums, queries)
print(res)
print(output)
print(res == output)
