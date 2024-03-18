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


class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        steps = 1
        while True:
            val = nums[i]
            if i + val >= len(nums)-1:
                break
            longest = 0
            for j in range(i+1, i+1+val):
                reach = nums[j] + (j - i)
                if i == 1:
                    print(i+1, i+1+val)
                    print(i, j, val, longest, reach)
                if reach > longest:
                    i = j
                    longest = reach
            steps += 1
        return steps


obj = Solution()
result = obj.jump(nums)
print(result)
