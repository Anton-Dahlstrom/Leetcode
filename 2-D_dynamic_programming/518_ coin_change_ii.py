import heapq
import copy


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        coins.sort()
        self.res = 0
        hmap = {}
        for i, c in enumerate(coins):
            hmap[c] = [[0]*len(coins)]
            hmap[c][0][i] += 1
            # counter[c] = 1

        heap = coins.copy()
        heapq.heapify(heap)

        while heap:
            cur = heapq.heappop(heap)
            combination = hmap.pop(cur)
            if cur == amount:
                return len(combination)
            for i, c in enumerate(coins):
                val = cur + c
                if val <= amount:
                    curComb = combination.copy()
                    if val in hmap:
                        for comb in curComb:
                            comb[i] += 1
                            if comb not in hmap[val]:
                                hmap[val].append(comb.copy())
                    else:
                        hmap[val] = []
                        for comb in curComb:
                            comb[i] += 1
                            hmap[val].append(comb.copy())
                        heapq.heappush(heap, val)

        return -1

        # self.res = 0
        # def dfs(i, cur):
        #     print(cur)
        #     if cur == 0:
        #         self.res += 1
        #         return
        #     for j in range(i, len(coins)):
        #         val = cur - coins[j]
        #         if val < 0:
        #             return
        #         dfs(j, val)
        # dfs(0, amount)
        # return self.res


amount = 20
coins = [3, 5, 7, 8, 9, 10, 11]
output = 20

amount = 5
coins = [1, 2, 5]
output = 4


obj = Solution()
res = obj.change(amount, coins)
print(res)
print(res == output)
