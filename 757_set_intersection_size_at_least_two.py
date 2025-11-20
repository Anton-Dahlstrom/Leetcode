class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        nums = [float("-inf"), float("-inf")]
        for start, end in intervals:
            if start > nums[1]:
                nums = [end-1, end]
                res += 2
            elif start > nums[0]:
                if end == nums[1]:
                    nums = [end-1, end]
                else:
                    nums = [nums[1], end]
                res += 1
        return res


intervals = [[1, 3], [3, 7], [5, 7], [7, 8]]
output = 5

obj = Solution()
res = obj.intersectionSizeTwo(intervals)
print(res)
print(output)
print(res == output)
