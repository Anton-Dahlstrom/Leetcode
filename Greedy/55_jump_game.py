from typing import List

nums = [3, 2, 1, 0, 4]
# nums = [2, 3, 1, 1, 4]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        visited = {}
        result = self.jump(i, nums, visited)
        return result

    def jump(self, i, nums, visited):
        if i in visited:
            return False
        else:
            visited[i] = 1

        goal = len(nums) - 1
        if i <= goal:
            jumps = nums[i]
        else:
            jumps = goal - i

        if i == goal:
            return True
        for j in reversed(range(1, jumps + 1)):
            if j == goal:
                return True
            result = self.jump(i + j, nums, visited)
            if result:
                return True
        return False


obj = Solution()
result = obj.canJump(nums)
print(result)
