class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        res = 0
        n = len(tasks)
        for i in range(0, n, 4):
            res = max(res, tasks[i] + processorTime[i // 4])
        return res


processorTime = [8, 10]
tasks = [2, 2, 3, 1, 8, 7, 4, 5]
output = 16

obj = Solution()
res = obj.minProcessingTime(processorTime, tasks)
print(res)
print(output)
print(res == output)
