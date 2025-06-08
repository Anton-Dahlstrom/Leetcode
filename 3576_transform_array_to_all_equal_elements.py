class Solution:
    def canMakeEqual(self, nums: list[int], k: int) -> bool:
        prevpos = -1
        posdist = 0

        prevneg = -1
        negdist = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                if prevpos < 0:
                    prevpos = i
                else:
                    posdist += i - prevpos
                    prevpos = -1
            else:
                if prevneg < 0:
                    prevneg = i
                else:
                    negdist += i - prevneg
                    prevneg = -1

        if (prevpos < 0 and posdist <= k) or (prevneg < 0 and negdist <= k):
            return True
        return False


nums = [-1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1]
k = 3
output = False

obj = Solution()
res = obj.canMakeEqual(nums, k)
print(res)
print(output)
print(res == output)
