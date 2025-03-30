class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ends = {}
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] not in ends:
                ends[s[i]] = i
        res = []
        last = 0
        total = -1
        for i in range(n):
            last = max(last, ends[s[i]])
            if i == last:
                res.append(i-total)
                total = i
        return res


s = "ababcbacadefegdehijhklij"
output = [9, 7, 8]
obj = Solution()
res = obj.partitionLabels(s)
print(res)
print(res == output)
