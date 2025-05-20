class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def getDigitSum(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        n = len(nums)
        rank = [0] * n
        for i in range(n):
            digitSum = getDigitSum(nums[i])
            rank[i] = [digitSum, nums[i], i]
        rank.sort()

        for i in range(n):
            finalIndex = i
            curIndex = rank[i][2]
            nums[curIndex] = finalIndex
        res = 0

        for i in range(n):
            while nums[i] != i:
                res += 1
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return res


nums = [978678783, 989995084, 465932830, 37255967]
output = 3

obj = Solution()
res = obj.minSwaps(nums)
print(res)
print(output)
print(res == output)
