class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        curTotal = 0
        count = {}

        # Add first range of numbers to hashmap
        for i in range(k):
            curTotal += nums[i]
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        # Update res if all numbers are unique
        if len(count) == k:
            res = max(res, curTotal)

        # Remove and add one number at a time and update res when all numbers are unique.
        for i in range(k, len(nums)):
            removing = nums[i-k]
            count[removing] -= 1
            if not count[removing]:
                count.pop(removing)

            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

            curTotal -= removing
            curTotal += nums[i]
            if len(count) == k:
                res = max(res, curTotal)
        return res


nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
output = 15

obj = Solution()
res = obj.maximumSubarraySum(nums, k)
print(res)
print(output)
print(res == output)
