from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def dfs(s: str, index):
            for i in range(index+1, len(s)+1):
                print(index, i)
                print(s[index: i])
                if checkPalindrome(s[index:i]):
                    temp.append(s[index:i])
                    if i == len(s):
                        print("APPENDING: ", temp)
                        res.append(temp)
                    else:
                        dfs(s, i+1)
                    temp.pop()

        def checkPalindrome(s: str):
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

        dfs(s, 0)
        return res


s = "aab"
Output = [["a", "a", "b"], ["aa", "b"]]

obj = Solution()
res = obj.partition(s)
print(res)
