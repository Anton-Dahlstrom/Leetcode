class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        maxSum = nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3]
        if maxSum < target:
            return maxSum

        l, m, r = 0, 1, 2
        diff = float("inf")
        res = 0

        tempDiff = 0
        absDiff = diff

        for l in range(len(nums)-2):
            minSum = nums[l] + nums[l+1] + nums[l+2]
            if l < len(nums)-3 and minSum > target:
                tempDiff = minSum - target
                absDiff = abs(minSum - target)
                if absDiff < diff:
                    diff = absDiff
                    res = minSum
                continue
            m = l+1
            while m < len(nums)-1:
                r = m+1
                total = nums[l] + nums[m] + nums[r]
                tempDiff = total - target
                absDiff = abs(total - target)
                if tempDiff > 0 and absDiff >= diff:
                    break
                if absDiff < diff:
                    diff = absDiff
                    res = total
                while r < len(nums)-1:
                    r += 1
                    total = nums[l] + nums[m] + nums[r]
                    tempDiff = total - target
                    absDiff = abs(total - target)
                    if tempDiff > 0 and absDiff >= diff:
                        break
                    if absDiff < diff:
                        diff = absDiff
                        res = total
                m += 1
        return res


nums = [-84, 92, 26, 19, -7, 9, 42, -51, 8, 30, -100, -13, -38]
target = 78
output = 77


obj = Solution()
res = obj.threeSumClosest(nums, target)
print(res)
print(output)
print(res == output)
