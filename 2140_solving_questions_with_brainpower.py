class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        questions.append([0, 0])
        cur = 0
        for i in range(n):
            point = questions[i][0]
            delay = questions[i][1]
            if len(questions[i]) == 3:
                cur = max(cur, questions[i][2])
            point += cur
            nextq = min(i+delay+1, n)
            if len(questions[nextq]) == 2:
                questions[nextq].append(point)
            else:
                questions[nextq][2] = max(questions[nextq][2], point)

        return questions[-1][0] + questions[-1][2]


questions = [[21, 5], [92, 3], [74, 2], [
    39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]
output = 157


obj = Solution()
res = obj.mostPoints(questions)
print(res)
print(output)
print(res == output)
