from collections import deque


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        queue = deque([[-1, 0, -1], [-1, 0, -1]])
        res = 0
        for i in range(n):
            fruit = fruits[i]
            if fruit == queue[0][0]:
                queue[0][2] = i
            elif fruit == queue[1][0]:
                queue[1][2] = i
            else:
                if queue[0][2] < queue[1][2]:
                    queue[1][1] = queue[0][2]+1
                    queue.popleft()
                else:
                    queue[0][1] = queue[1][2]+1
                    queue.pop()
                queue.append([fruit, i, i])
            res = max(res, i-min(queue[1][1], queue[0][1])+1)
        return res


fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
output = 5

fruits = [1, 2, 1]
output = 3

obj = Solution()
res = obj.totalFruit(fruits)
print(res)
print(output)
print(res == output)
