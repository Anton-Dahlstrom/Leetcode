class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        def validMutation(g1, g2):
            diff = 0
            for i in range(8):
                if g1[i] != g2[i]:
                    if diff > 0:
                        print(diff)
                        return False
                    diff += 1
            return True

        bank = [startGene] + bank
        indexes = [i for i in range(1, len(bank)) if bank[i] != startGene]

        arr = [0]
        steps = 0
        while arr:
            steps += 1
            temp = []
            while arr:
                cur = arr.pop()
                p = 0
                while p < len(indexes):
                    i = indexes[p]
                    if validMutation(bank[cur], bank[i]):
                        if bank[i] == endGene:
                            return steps
                        temp.append(indexes.pop(p))
                        continue
                    p += 1
            arr = temp
        return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
output = 2

obj = Solution()
res = obj.minMutation(startGene, endGene, bank)
print(res)
print(output)
print(res == output)
