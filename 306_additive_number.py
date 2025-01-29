class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        if len(num) < 3:
            return False
        if int(num) == 0:
            return True

        def dfs(prev, val, i):
            if i == len(num):
                return True
            target = prev+val
            l = i
            if num[l] == "0":
                return False

            r = l+1
            while r <= len(num):
                cur = int(num[l:r])
                if cur == target:
                    if dfs(val, target, r):
                        return True
                elif cur > target:
                    return False
                r += 1
            return False
        if num[0] == "0":
            if dfs(0, int(num[1]), 2):
                return True
            return False

        for i in range(1, (len(num)//2)+1):
            if num[i] == "0":
                if dfs(int(num[0:i]), int(num[i]), i+1):
                    return True
                continue
            for j in range(i+1, len(num)):
                if dfs(int(num[0:i]), int(num[i:j]), j):
                    return True

        return False


num = "199111992"
output = True

obj = Solution()
res = obj.isAdditiveNumber(num)
print(res)
print(output)
print(res == output)
