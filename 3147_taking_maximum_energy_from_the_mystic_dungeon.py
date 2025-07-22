class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        total = [0] * k
        for i, e in enumerate(energy):
            total[i % k] = max(e, total[i % k] + e)
        return max(total)


energy = [-2, -3, -1]
k = 2
output = -1

obj = Solution()
res = obj.maximumEnergy(energy, k)
print(res)
print(output)
print(res == output)
