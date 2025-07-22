class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        total = [0] * k
        res = energy[-1]
        for i in range(n):
            total[i % k] = max(energy[i], total[i % k] + energy[i])
            res = max(res, total[i % k])
        return max(total)


energy = [-2, -3, -1]
k = 2
output = -1

obj = Solution()
res = obj.maximumEnergy(energy, k)
print(res)
print(output)
print(res == output)
