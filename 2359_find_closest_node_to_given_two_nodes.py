class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        visit1 = set()
        visit2 = set()
        cur1 = node1
        cur2 = node2
        res = 0
        while True:
            if cur1 == cur2:
                return cur1
            if cur1 in visit2 and cur2 in visit1:
                return min(cur1, cur2)
            elif cur1 in visit2:
                return cur1
            elif cur2 in visit1:
                return cur2
            if cur1 in visit1 and cur2 in visit2 or (cur1 in visit1 and cur2 == -1) or (cur2 in visit2 and cur1 == -1):
                return -1
            res += 1
            if cur1 == -1 and cur2 == -1:
                return -1
            if cur1 != -1:
                visit1.add(cur1)
                cur1 = edges[cur1]
            if cur2 != -1:
                visit2.add(cur2)
                cur2 = edges[cur2]


edges = [1, 2, -1]
node1 = 0
node2 = 2
output = 2

edges = [2, 2, 3, -1]
node1 = 0
node2 = 1
output = 2

obj = Solution()
res = obj.closestMeetingNode(edges, node1, node2)
print(res)
print(output)
print(res == output)
