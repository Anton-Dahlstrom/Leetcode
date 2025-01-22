class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        indexes = [i for i in range(len(people))]
        res = [0]*len(people)
        people.sort()
        counter = 0
        for i, p in enumerate(people):
            height, pos = p
            if i > 0:
                if people[i-1][0] == height:
                    counter += 1
                else:
                    counter = 0
            index = indexes.pop(pos-counter)
            res[index] = [height, pos]

        return res


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
output = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]


obj = Solution()
res = obj.reconstructQueue(people)
print(res)
print(output)
print(res == output)
