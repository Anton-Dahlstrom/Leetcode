import math


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:

        def bruteForce(time):
            serviced = 0
            for rank in ranks:
                n = math.isqrt(time//rank)
                serviced += n
                if serviced >= cars:
                    return True
            return False

        l = 0
        r = (((cars//len(ranks)) + 1)**2) * max(ranks)
        while l < r:
            mid = l + ((r-l)//2)
            if not bruteForce(mid):
                l = mid+1
            else:
                r = mid
        return r


ranks = [4, 2, 3, 1]
cars = 10
output = 16

obj = Solution()
res = obj.repairCars(ranks, cars)
print(res)
print(output)
print(res == output)
