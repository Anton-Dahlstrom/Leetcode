class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        source = {}
        for time in times:
            source.setdefault(time[0], {})
            if time[1] not in source[time[0]]:
                source[time[0]][time[1]] = time[2]
            else:
                source[time[0]][time[1]] = min(
                    time[2], source[time[0]][time[1]])
        if k not in source:
            return -1

        shortest = {}

        def dfs(node, cur):
            if node in source:
                for edge in source[node]:
                    temp = cur + source[node][edge]
                    if edge not in shortest:
                        shortest[edge] = temp
                        dfs(edge, temp)
                    elif temp < shortest[edge]:
                        shortest[edge] = temp
                        dfs(edge, temp)

        shortest[k] = 0
        dfs(k, 0)

        if len(shortest) == n:
            return max(shortest.values())
        return -1


times = [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75], [5, 1, 15], [
    1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51], [3, 1, 36], [2, 3, 59]]
n = 5
k = 5
output = 31

obj = Solution()
res = obj.networkDelayTime(times, n, k)
print(res)
print(res == output)
