import heapq


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        heap = [0]
        hmap = {0: {0}}
        while heap:
            cur = heapq.heappop(heap)
            combinations = hmap.pop(cur)
            if cur == amount:
                return len(combinations)
            for c in coins:
                val = cur + c
                if val <= amount:
                    if val not in hmap:
                        temp = set()
                        for comb in combinations:
                            temp.add(comb+(c ** 6))
                        hmap[val] = temp
                        heapq.heappush(heap, val)
                    else:
                        for comb in combinations:
                            updatedComb = comb + (c ** 6)
                            if updatedComb not in hmap[val]:
                                hmap[val].add(updatedComb)

        return 0

        # Need to add the coins sequentially to avoid having to keep track
        # of unique combinations of coins.
        # Will try with a large array and carrying previous results forward,
        # intuition tells me i might have to start from the end and keep
        # track of previously visited indexes with the current coin.

        # matrix = [1,3,4]

        # adding 1
        # var = {0:0, 1:1, 2:1, 3:1, 4:1, 5:1 , 6:1, 7:1, 8:1, 9:1, 10:1}
        # adding 3
        # var = {0:0, 1:1, 2:1, 3:2, 4:2, 5:2 , 6:3, 7:3, 8:3, 9:4, 10:4}

        # paths to 10:
        # 1*10
        # 1*1 + 3*3
        # 1*4 + 3*2
        # 1*7 + 3*1
        # 1*3 + 3*1 + 4*1
        # 1*2 + 4*2
        # 1*6 + 4*1
        # 3*2 + 4*1


amount = 10
coins = [1, 3, 4]
output = 8

# amount = 5
# coins = [1, 2, 5]
# output = 4

# amount = 500
# coins = [1, 2, 5]
# output = 12701

# amount = 100
# coins = [3, 5, 7, 8, 9, 10, 11]
# output = 6606

# amount = 500
# coins = [3, 5, 7, 8, 9, 10, 11]
# output = 35502874

obj = Solution()
res = obj.change(amount, coins)
print(res)
print(res == output)
