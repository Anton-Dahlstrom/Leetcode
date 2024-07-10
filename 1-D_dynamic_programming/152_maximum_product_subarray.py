from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def maxOrNone(values):
            candidates = [val for val in values if val is not None]
            return max(candidates) if candidates else None

        res = positive = negative = None
        tempPos = None
        for val in nums:
            print(res, positive, negative)
            if val == 0:
                res = maxOrNone(
                    [0, res, positive, negative])
                positive = negative = None
                continue
            res = maxOrNone(
                [res, positive, negative])

            if val < 0:
                if negative:
                    tempPos = negative * val
                if positive:
                    negative = positive * val
                else:
                    negative = val
                positive = tempPos
                tempPos = None
            else:
                if positive:
                    positive *= val
                else:
                    positive = val
                if negative:
                    negative *= val

        print(res, positive, negative)
        res = maxOrNone([res, positive, negative])
        return res


# nums = [-2, 0, -1]
# output = 0

nums = [2, -5, -2, -4, 3]
output = 24


obj = Solution()
res = obj.maxProduct(nums)
print(res)
print(res == output)
