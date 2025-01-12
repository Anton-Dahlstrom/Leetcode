class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        moves = [0]*(len(s)+1)
        for shift in shifts:
            left, right, direction = shift
            if direction:
                moves[left] += 1
                moves[right+1] -= 1
            else:
                moves[left] -= 1
                moves[right+1] += 1
        s = [ord(c) for c in s]
        cur = 0
        for i in range(len(s)):
            cur += moves[i]
            if cur < -26:
                cur %= -26
            elif cur > 26:
                cur %= 26
            s[i] += cur
            if s[i] < 97:
                s[i] = 123 - (97 - s[i])
            elif s[i] > 122:
                s[i] = 96 + (s[i] - 122)
            s[i] = chr(s[i])
        return "".join(s)


s = "dztz"
shifts = [[0, 0, 0], [1, 1, 1]]
output = "catz"


obj = Solution()
res = obj.shiftingLetters(s, shifts)
print(res)
print(output)
print(res == output)
