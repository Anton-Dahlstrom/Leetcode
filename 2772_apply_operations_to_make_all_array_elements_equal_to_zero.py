class Solution:
    def checkArray(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        cur = 0
        diff = [0] * (n+1)
        for i in range(n):
            cur -= diff[i]
            if cur > nums[i]:
                return False
            index = i+k
            if index > n:
                if cur != nums[i]:
                    return False
                continue
            removing = nums[i] - cur
            cur += removing
            diff[index] = removing

        return True


nums = [63, 40, 30, 0, 72, 53]
k = 1
output = True

obj = Solution()
res = obj.checkArray(nums, k)
print(res)
print(output)
print(res == output)
