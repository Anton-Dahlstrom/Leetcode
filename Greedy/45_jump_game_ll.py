from typing import List

nums = [2, 3, 1, 1, 4]
Output: 2

# nums = [2, 3, 0, 1, 4]
# Output: 2

# nums = [1, 2]
# Output: 1


class Solution:
    def jump(self, nums: List[int]) -> int:
        largest = 0
        for num in nums:
            if num > largest:
                largest = num

        i = 0
        visited = {}
        result = self.recurJump(i, nums, 0, visited, largest)
        return result

    def recurInverseJump(self, i, nums, timesJumped, visisted, largest):
        goal = 0
        length = len(nums)
        if i >= goal:
            jumps = nums[i]
            timesJumped

        shortest = float("inf")
        for j in reversed(range(1, largest)):
            if i - j > 0:
                if nums[i-j] >= j:
                    result = self.recurInverseJump()
                    shortest = min(result, shortest)
            else:
                continue
        return result

    def recurJump(self, i, nums, timesJumped, visited, largest):
        goal = len(nums) - 1

        if i <= goal:
            jumps = nums[i]
        else:
            jumps = goal - i

        if i == goal:
            print(timesJumped, "hi")
            return timesJumped

        shortest = float("inf")
        for j in reversed(range(1, jumps + 1)):
            print(i, j)
            if j == goal:
                return timesJumped + 1
            if i + j in visited:
                if timesJumped + 1 >= visited[i+j]:
                    continue
            else:
                visited[i + j] = timesJumped + 1
            result = self.recurJump(i + j, nums, timesJumped + 1, visited)
            print(result, shortest)
            shortest = min(result, shortest)

        return shortest


obj = Solution()
result = obj.jump(nums)
print(result)
