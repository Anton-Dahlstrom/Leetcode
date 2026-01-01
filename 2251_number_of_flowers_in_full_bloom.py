class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        # time, event
        events = []
        for start, stop in flowers:
            events.append((start, 1))
            events.append((stop+1, -1))
        for i, p in enumerate(people):
            events.append((p, 2, i))
        events.sort()
        res = [0]*len(people)
        cur = 0
        for e in events:
            if len(e) == 3:
                time, event, index = e
                res[index] = cur
            else:
                time, event = e
                cur += event
        return res


flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
people = [2, 3, 7, 11]
output = [1, 2, 2, 2]

obj = Solution()
res = obj.fullBloomFlowers(flowers, people)
print(res)
print(output)
print(res == output)
