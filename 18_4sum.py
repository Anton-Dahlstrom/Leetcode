class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        lastAdded = []
        l = 0
        while l < len(nums)-3:
            lm = l+1
            while lm < len(nums)-2:
                rm = lm+1
                while rm < len(nums)-1:
                    r = rm+1
                    while r < len(nums):
                        total = nums[l] + nums[lm] + nums[rm] + nums[r]
                        if total > target:
                            break
                        if total == target:
                            temp = [nums[l], nums[lm], nums[rm], nums[r]]
                            if temp != lastAdded:
                                lastAdded = temp
                                res.append(temp)
                        next = r+1
                        while next < len(nums) and nums[r] == nums[next]:
                            next += 1
                        r = next 

                    next = rm+1
                    while next < len(nums) and nums[rm] == nums[next]:
                        next += 1 
                    rm = next 
                next = lm+1
                while next < len(nums) and nums[lm] == nums[next]:
                    next += 1 
                lm = next 
            next = l+1
            while next < len(nums) and nums[l] == nums[next]:
                next += 1 
            l = next 
        return res

nums = [1,0,-1,0,-2,2]
target = 0
output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

nums = [0,0,0,0]
target = 0
output = [[0,0,0,0]]

obj = Solution()
res = obj.fourSum(nums, target)
print(res)
print(output)
print(res == output)