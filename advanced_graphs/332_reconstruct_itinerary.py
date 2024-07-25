class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        departures = {}
        arrivals = {}
        for dep, arr in tickets:
            departures.setdefault(dep, []).append(arr)
            arrivals.setdefault(arr, []).append(dep)
        res = ["JFK"]

        for k in departures:
            departures[k].sort()

        def dfsBacktrack(airport):
            if len(res) == len(tickets)+1:
                return True
            if airport in departures:
                prev = None
                for i in range(len(departures[airport])):
                    next = departures[airport][i]
                    if not next or next == prev:
                        continue
                    prev = next
                    departures[airport][i] = None
                    res.append(next)
                    if dfsBacktrack(next):
                        return True
                    departures[airport][i] = next
                    res.pop()
        dfsBacktrack(res[0])
        return res


tickets = [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"],
           ["TIA", "ANU"], ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]]
output = ["JFK", "ANU", "EZE", "AXA", "TIA",
          "ANU", "JFK", "TIA", "ANU", "TIA", "JFK"]

obj = Solution()
res = obj.findItinerary(tickets)
print(res)
print(res == output)
