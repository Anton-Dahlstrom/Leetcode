class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        res = float("inf")
        hmap = {}
        for i, card in enumerate(cards):
            if card in hmap:
                res = min(res, i - hmap[card] + 1)
            hmap[card] = i
        if res == float("inf"):
            return -1
        return res


cards = [95, 11, 8, 65, 5, 86, 30, 27, 30, 73, 15, 91,
         30, 7, 37, 26, 55, 76, 60, 43, 36, 85, 47, 96, 6]
output = 3

obj = Solution()
res = obj.minimumCardPickup(cards)
print(res)
print(output)
print(res == output)
