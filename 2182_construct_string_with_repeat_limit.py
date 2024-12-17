class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hmap = {}
        res = ""
        for char in s:
            hmap.setdefault(char, 0)
            hmap[char] += 1
        stack = [[key, hmap[key]] for key in hmap]
        stack.sort()
        i = len(stack)-1
        count = 0
        while i >= 0:
            popping = i
            count += 1
            if count > repeatLimit:
                popping -= 1
                count = 0
            if popping < 0:
                return res
            res += stack[popping][0]
            stack[popping][1] -= 1
            if stack[popping][1] <= 0:
                stack.pop(popping)
                count = 0
                i -= 1

        return res


s = "cczazcc"
repeatLimit = 3
output = "zzcccac"

s = "robnsdvpuxbapuqgopqvxdrchivlifeepy"
repeatLimit = 2
output = "yxxvvuvusrrqqppopponliihgfeeddcbba"

obj = Solution()
res = obj.repeatLimitedString(s, repeatLimit)
print(res)
print(output)
print(res == output)
