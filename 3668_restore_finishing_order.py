class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        friends = set(friends)
        res = []
        for o in order:
            if o in friends:
                res.append(o)
        return res


order = [3, 1, 2, 5, 4]
friends = [1, 3, 4]
output = [3, 1, 4]

obj = Solution()
res = obj.recoverOrder(order, friends)
print(res)
print(output)
print(res == output)
