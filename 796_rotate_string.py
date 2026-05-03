class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(goal)
        for i in range(n):
            if s[i:] + s[:i] == goal:
                return True
        return False
