class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        swap = -1
        for i in reversed(range(1, len(nums))):
            if nums[i] > nums[i-1]:
                swap = i-1
                break
        if swap == -1:
            nums.sort()
            return 
        val = float("inf")
        swap2 = 0

        for j in range(swap+1, len(nums)):
            if nums[j] > nums[swap] and nums[j] < val:
                swap2 = j
                val = nums[j]

        nums[swap], nums[swap2] = nums[swap2], nums[swap]
        nums[swap+1:] = sorted(nums[swap+1:])
        return


nums = [1,2,3]
output = [1,3,2]

obj = Solution()
obj.nextPermutation(nums)
print(nums)
print(nums == output)