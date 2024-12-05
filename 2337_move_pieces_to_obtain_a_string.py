class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def findNextChar(string, i):
            while i < len(string):
                if string[i] == "_":
                    i += 1
                else:
                    return i
            return i

        si, ti = -1, -1
        while True:
            si = findNextChar(start, si+1)
            ti = findNextChar(target, ti+1)

            # All chars could be moved
            if si >= len(start) and ti >= len(target):
                return True

            # Uneven amount of chars
            if si >= len(start) or ti >= len(target):
                return False

            # Start-char can't move in the right direction or the chars don't match. (Order can't be swapped)
            if (start[si] == "L" and si < ti) or (start[si] == "R" and si > ti) or start[si] != target[ti]:
                return False


start = "_L__R__RL"
target = "L_____RLR"
output = False


obj = Solution()
res = obj.canChange(start, target)
print(res)
print(output)
print(res == output)
