class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        res = 0
        for fruit in fruits:
            found = False
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    found = True
                    break
            if not found:
                res += 1
        return res


fruits = [4, 2, 5]
baskets = [3, 5, 4]

output = 1

obj = Solution()
res = obj.numOfUnplacedFruits(fruits, baskets)
print(res)
print(output)
print(res == output)
