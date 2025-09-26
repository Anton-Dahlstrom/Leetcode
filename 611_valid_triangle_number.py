class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                val = nums[i] + nums[j]
                l = j
                r = n-1
                while l <= r:
                    mid = l+((r-l)//2)
                    if nums[mid] >= val:
                        r = mid - 1
                    else:
                        l = mid + 1
                res += max(0, l-1-j)
        return res


nums = [2, 2, 3, 4]
output = 3

obj = Solution()
res = obj.triangleNumber(nums)
print(res)
print(output)
print(res == output)
