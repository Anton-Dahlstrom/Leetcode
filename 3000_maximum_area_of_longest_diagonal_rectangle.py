class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        biggest = 0
        res = 0
        for length, width in dimensions:
            size = (length**2) + (width**2)
            if size > biggest:
                biggest = size
                res = length * width
            elif size == biggest:
                res = max(res, length*width)
        return res


dimensions = [[9, 3], [8, 6]]
output = 48

obj = Solution()
res = obj.areaOfMaxDiagonal(dimensions)
print(res)
print(output)
print(res == output)
