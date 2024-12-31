import heapq


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        daypasses = [1, 7, 30]
        cheapest = [float("inf")]*(len(days) + 1)
        heap = [[0, 0]]  # cost so far, next index

        def moveIndex(cost, i, price, daypass):
            maxdays = days[i] + daypass
            i += 1
            while i < len(days):
                if days[i] < maxdays:
                    cheapest[i] = min(cheapest[i], cost+price)
                    i += 1
                else:
                    break
            return [cost+price, i]

        while heap:
            cost, i = heapq.heappop(heap)
            for j in range(len(costs)):
                newcost, newi = moveIndex(cost, i, costs[j], daypasses[j])
                if newcost < cheapest[newi]:
                    cheapest[newi] = newcost
                    if newi < len(days):
                        heapq.heappush(heap, [newcost, newi])
        return cheapest[-1]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
output = 11


obj = Solution()
res = obj.mincostTickets(days, costs)
print(res)
print(output)
print(res == output)
