from typing import List

s = "aab"
output = [["a", "a", "b"], ["aa", "b"]]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.temp = []
        self.dfs(s, 0)
        return self.res

    def dfs(self, s: str, index):
        for i in range(index, len(s)+1):
            if self.checkPalindrome(s[index:i+1]):
                self.temp.append(s[index:i+1])
                if i == len(s):
                    self.res.append(self.temp.copy())
                else:
                    self.dfs(s, i+1)
                self.temp.pop()

    def checkPalindrome(self, s: str):
        if not s:
            return False
        l = len(s)//2
        r = len(s)//2
        if not len(s) % 2:
            l -= 1
        while l >= 0:
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                return False
        return True


s = "aab"
Output = [["a", "a", "b"], ["aa", "b"]]

obj = Solution()
res = obj.partition(s)
print(res)
