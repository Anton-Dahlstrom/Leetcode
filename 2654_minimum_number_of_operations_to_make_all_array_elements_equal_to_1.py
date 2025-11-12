class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        def gcd(a, b):
            while a and b:
                a %= b
                a, b = b, a
            return a

        if nums.count(1):
            return n - nums.count(1)

        states = [nums.copy()]
        visited = set()
        res = 0
        while states:
            temp = []
            while states:
                base = states.pop()
                for i in range(n):
                    cur = base.copy()
                    if i > 0 and cur[i] != cur[i-1]:
                        cur[i] = gcd(cur[i], cur[i-1])
                        if cur[i] == 1:
                            return res + n
                        state = tuple(cur)
                        if state not in visited:
                            visited.add(state)
                            temp.append(cur)

                    cur = base.copy()
                    if i < n-1 and cur[i] != cur[i+1]:
                        cur[i] = gcd(cur[i], cur[i+1])
                        if cur[i] == 1:
                            return res + n
                        state = tuple(cur)
                        if state not in visited:
                            visited.add(state)
                            temp.append(cur)
            states = temp
            res += 1
        return -1


nums = [2, 6, 3, 4]
output = 4


obj = Solution()
res = obj.minOperations(nums)
print(res)
print(output)
print(res == output)
