class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = set()
        arr = []

        def dfs(i):
            if i == len(pattern):
                return True
            for num in range(1, 10):
                if num not in used:
                    if not arr:
                        used.add(num)
                        arr.append(num)
                        used.add(num)
                        if dfs(i+1):
                            return True
                        used.remove(num)
                        arr.pop()
                    else:
                        if (pattern[i] == "I" and num > arr[-1]) or (pattern[i] == "D" and num < arr[-1]):
                            used.add(num)
                            arr.append(num)
                            if dfs(i+1):
                                return True
                            arr.pop()
                            used.remove(num)

            return False
        dfs(-1)
        return "".join([str(n) for n in arr])


pattern = "IIIDIDDD"
output = "123549876"

obj = Solution()
res = obj.smallestNumber(pattern)
print(res)
print(output)
print(res == output)
