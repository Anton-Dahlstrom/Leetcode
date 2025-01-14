class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = [[a, "a"], [b, "b"], [c, "c"]]
        arr.sort(reverse=True)

        repetition = 0
        res = ""
        prev = ""
        while True:
            print(repetition)
            if repetition >= 1 and arr[0][1] == prev:
                char = arr[1]
            else:
                char = arr[0]

            if char[1] == prev:
                repetition +=1
            else:
                repetition = 0 
            if not char[0]:
                return res
            prev = char[1]
            res += char[1]
            char[0] -= 1
            arr.sort(reverse=True)


a = 3
b = 3
c = 9
output = "ccaccbccaccbbac"

obj = Solution()
res = obj.longestDiverseString(a, b, c)
print(res)
print(output)
print(res == output)