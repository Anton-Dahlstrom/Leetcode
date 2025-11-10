class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        stack = [0]
        for i in range(n):
            num = nums[i]
            while stack and stack[-1] > num:
                stack.pop()
                res += 1
            if not stack or stack[-1] < num:
                stack.append(num)
        res += len(stack) - 1

        return res


nums = [1, 2, 1, 2, 1, 2]
output = 4

obj = Solution()
res = obj.minOperations(nums)
print(res)
print(output)
print(res == output)
