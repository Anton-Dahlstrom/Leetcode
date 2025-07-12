class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = min(prefix[i-1], nums[i])

        postfix = [0] * n
        postfix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            postfix[i] = min(postfix[i+1], nums[i])

        res = float("inf")
        for i in range(1, n-1):
            if prefix[i-1] >= nums[i] or postfix[i+1] >= nums[i]:
                continue
            size = prefix[i-1] + nums[i] + postfix[i+1]
            res = min(size, res)

        if res == float("inf"):
            res = -1
        return res


nums = [5, 4, 8, 7, 10, 2]
output = 13

obj = Solution()
res = obj.minimumSum(nums)
print(res)
print(output)
print(res == output)
