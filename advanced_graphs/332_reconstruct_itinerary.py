class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        departures = {}
        arrivals = {}
        for dep, arr in tickets:
            departures.setdefault(dep, []).append(arr)
            arrivals.setdefault(arr, []).append(dep)
        res = ["JFK"]

        def dfsBacktrack(airport):
            if len(res) == len(tickets)+1:
                return True
            if airport in departures:
                departures[airport].sort(reverse=True)
                for i in reversed(range(len(departures[airport]))):
                    next = departures[airport].pop(i)
                    res.append(next)
                    if dfsBacktrack(next):
                        return True
                    departures[airport].append(next)
                    res.pop()

        dfsBacktrack(res[0])
        return res


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
output = ["JFK", "MUC", "LHR", "SFO", "SJC"]

tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
output = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]

tickets = [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"],
           ["TIA", "ANU"], ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]]
output = ["JFK", "ANU", "EZE", "AXA", "TIA",
          "ANU", "JFK", "TIA", "ANU", "TIA", "JFK"]

obj = Solution()
res = obj.findItinerary(tickets)
print(res)
print(res == output)
