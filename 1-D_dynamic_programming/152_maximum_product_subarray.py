from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def maxOrNone(values):
            candidates = [val for val in values if val is not None]
            return max(candidates) if candidates else None
        res = negative = prevPositive = curPositive = None
        for val in nums:
            if val == 0:
                res = maxOrNone([0, res, negative, prevPositive, curPositive])
                negative = prevPositive = curPositive = None
                continue
            elif val < 0:
                if negative:
                    negative *= val
                    if prevPositive:
                        negative *= prevPositive
                    if curPositive:
                        curPositive *= negative
                    else:
                        curPositive = negative
                    res = maxOrNone([res, negative, prevPositive, curPositive])
                    negative = None
                else:
                    prevPositive = curPositive
                    curPositive = None
                    negative = val
                continue
            if not curPositive:
                curPositive = val
            else:
                curPositive *= val
        res = maxOrNone([res, negative, prevPositive, curPositive])
        return res


nums = [2, 3, -2, 4]
output = 6

nums = [-2]
output = -2

nums = [-3, -1, -1]
output = 3

nums = [-2, 0, -1]
output = 0

nums = [-2, -3, 7]
output = 42

nums = [2, -5, -2, -4, 3]
output = 24

obj = Solution()
res = obj.maxProduct(nums)
print(res)
print(res == output)
