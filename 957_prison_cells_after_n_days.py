class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        visited = set()
        vals = []
        bitmask = 0
        for i in range(n):
            bitmask = 0
            temp = [0]*len(cells)
            for j in range(1, len(cells)-1):
                if cells[j-1] == cells[j+1]:
                    bitmask |= (1 << j-1)
                    temp[j] = 1
                else:
                    temp[j] = 0
            cells = temp
            if bitmask in visited:
                bitmask = vals[(n % i)-1]
                res = [0] + [1 if (bitmask >> i) & 1 ==
                             1 else 0 for i in range(0, len(cells)-2)] + [0]
                return res
            else:
                visited.add(bitmask)
                vals.append(bitmask)
        return temp


cells = [0, 1, 0, 1, 1, 0, 0, 1]
n = 7
output = [0, 0, 1, 1, 0, 0, 0, 0]

cells = [1, 0, 0, 1, 0, 0, 1, 0]
n = 1000000000
output = [0, 0, 1, 1, 1, 1, 1, 0]

obj = Solution()
res = obj.prisonAfterNDays(cells, n)
print(res)
print(output)
print(res == output)
