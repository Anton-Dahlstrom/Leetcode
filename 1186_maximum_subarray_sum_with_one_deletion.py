class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        cur = 0
        res = float("-inf")
        curdel = 0
        maxval = float("-inf")

        for i in range(len(arr)):
            num = arr[i]
            maxval = max(maxval, num)

            # Check if deleting the current num gives a better result.
            if cur - num > curdel:
                curdel = cur-num
            # Reset our deletion-sum.
            if curdel <= 0:
                curdel = 0

            cur += num
            curdel += num

            if cur < 0:
                cur = 0

            res = max(res, cur, curdel)

        if maxval < 0:
            return maxval
        return res


arr = [1, -200, 2, -200, 3]
output = 5


obj = Solution()
res = obj.maximumSum(arr)
print(res)
print(output)
print(res == output)
