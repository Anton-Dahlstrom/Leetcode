class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        source = {}
        target = {}
        for time in times:
            source.setdefault(time[0], {})
            if time[1] not in source[time[0]]:
                source[time[0]][time[1]] = time[2]
            else:
                source[time[0]][time[1]] = min(
                    time[2], source[time[0]][time[1]])

        targets = set()
        cur = k
        # Should probably search down from the root node and take each path.
        # If we reach a node that's not already in the root node's edges we add it
        # and set it's traveltime to the total traveltime it took to reach it through
        # this path.
        # If it's already connected to the root node we save the minimum traveltime.
        # Just need to make sure we don't dig in loops.
        return

        while cur:
            if cur not in targets:
                targets.add(cur)
                if cur in source:
                    for k in source[cur]:
                        pass


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
output = 2

obj = Solution()
res = obj.networkDelayTime(times, n, k)
print(res)
print(res == output)
