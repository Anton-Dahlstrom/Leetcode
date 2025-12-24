class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort()
        apples = sum(apple)
        res = 0
        while apples > 0:
            apples -= capacity.pop()
            res += 1
        return res


apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
output = 2

obj = Solution()
res = obj.minimumBoxes(apple, capacity)
print(res)
print(output)
print(res == output)
