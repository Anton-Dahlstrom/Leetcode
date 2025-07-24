class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        n = len(reward1)
        res = 0
        differences = [0]*n
        for i in range(n):
            differences[i] = reward1[i] - reward2[i]
            res += reward2[i]
        differences.sort(reverse=True)
        res += sum(differences[:k])
        return res


reward1 = [1, 1, 3, 4]
reward2 = [4, 4, 1, 1]
k = 2
output = 15

obj = Solution()
res = obj.miceAndCheese(reward1, reward2, k)
print(res)
print(output)
print(res == output)
