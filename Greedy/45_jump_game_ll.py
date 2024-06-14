from typing import List

nums = [2, 3, 1, 1, 4]
Output: 2

# nums = [2, 3, 0, 1, 4]
# Output: 2

# nums = [1, 2]
# Output: 1

nums = [3, 2, 1]
Output: 1

nums = [1, 2, 1, 1, 1]
Output: 3

# nums = [0]

# nums = [1, 2]


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        # The index we are jumping from
        cur = 0
        # Determines how far we can search
        reach = nums[0]
        # Keeps track of how far we searched last jump so we can start
        # from the index we stopped at before.
        jumps = 0
        while cur < len(nums):
            print(cur, len(nums))
            jumps += 1
            tempreach = reach
            for i in range(1, reach+1):
                if cur + i >= len(nums)-1:
                    print('hi')
                    return jumps
                # The index we are looking through will be further up in the list
                # and therefore reach further than our previous node.

                tempreach -= 1
                if nums[cur+i] + reach >= tempreach:
                    # This is wrong
                    tempreach = nums[cur+1] + reach
            cur = cur + reach
            reach = tempreach
            print(cur)
        return jumps


obj = Solution()
result = obj.jump(nums)
print(result)
