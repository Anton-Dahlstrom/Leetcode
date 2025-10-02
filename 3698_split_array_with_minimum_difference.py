class Solution:
    def splitArray(self, nums: list[int]) -> int:
        n = len(nums)
        lstop, rstop = n-1, 0
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                lstop = i-1
                break
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                print("hi")
                rstop = i+1
                break
        if lstop < rstop-1:
            return -1
        left = 0
        right = sum(nums)
        res = abs(right-left)
        for i in range(lstop+1):
            left += nums[i]
            right -= nums[i]
            if i >= rstop-1:
                res = min(res, abs(left-right))
                if left > right:
                    break
        return res


nums = [1, 2, 4, 3]
output = 4


# nums = [1, 2]
# output = 1

nums = [3, 1, 2]
output = -1

nums = [9, 10, 11, 5]
output = 3

# nums = [1, 3, 2]
# output = 2

nums = [9, 5, 4, 2]
output = 2

obj = Solution()
res = obj.splitArray(nums)
print(res)
print(output)
print(res == output)
