from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.length = len(digits)
        self.temp = "" 
        self.result = []
        if not digits:
            return self.result
        self.dfs(digits, 0)
        return self.result
    def dfs(self, digits, index):
        if index == self.length:
            self.result.append(self.temp)
            return
        num = int(digits[index])
        if num <= 1:
           return
        start = 1
        stop = 4
        if num == 7 or num == 9:
            stop +=1
        if num > 7:
            start += 1
            stop += 1
        for i in range(start,stop):
            self.temp += chr(90 + (num * 3) + i)
            self.dfs(digits, index+1)
            self.temp = self.temp[:-1]


obj = Solution()
res = obj.letterCombinations("9")
print(res)
