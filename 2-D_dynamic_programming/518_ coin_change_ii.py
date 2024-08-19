import copy
import heapq


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        heap = [0]
        base = ".".join([str(c-c) for c in coins])
        hmap = {0: {base}}
        while heap:
            asd = 6
            cur = heapq.heappop(heap)
            combinations = hmap.pop(cur)
            print(cur)
            # print(combinations)
            if cur == amount:
                return len(combinations)
            for i, c in enumerate(coins):
                val = cur + c
                if val <= amount:
                    if val not in hmap:
                        temp = set()
                        for comb in combinations:
                            combArr = comb.split(".")
                            newVal = int(combArr[i]) + 1
                            combArr[i] = str(newVal)
                            # combArr[i] += str(int(combArr[i]) + 1)
                            combHash = ".".join([str(v) for v in combArr])
                            temp.add(combHash)
                        hmap[val] = temp
                        heapq.heappush(heap, val)
                    else:
                        for comb in combinations:
                            combArr = comb.split(".")
                            newVal = int(combArr[i]) + 1
                            combArr[i] = str(newVal)
                            # combArr[i] += str(int(combArr[i]) + 1)
                            combHash = ".".join([str(v) for v in combArr])
                            if combHash not in hmap[val]:
                                hmap[val].add(combHash)

        return 0


amount = 20
coins = [3, 5, 7, 8, 9, 10, 11]
output = 20

amount = 5
coins = [1, 2, 5]
output = 4

amount = 500
coins = [1, 2, 5]
output = 12701

# amount = 100
# coins = [3, 5, 7, 8, 9, 10, 11]
# output = 6606

obj = Solution()
res = obj.change(amount, coins)
print(res)
print(res == output)
