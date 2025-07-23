class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        res = []
        for id, rating, vegan, price, dist in restaurants:
            if veganFriendly <= vegan and price <= maxPrice and dist <= maxDistance:
                res.append((rating, id))
        res.sort(reverse=True)
        res = [r[1] for r in res]
        return res


restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [
    3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10
output = [3, 1, 5]

obj = Solution()
res = obj.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance)
print(res)
print(output)
print(res == output)
