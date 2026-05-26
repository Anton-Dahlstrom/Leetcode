class Solution:
    def passwordStrength(self, password: str) -> int:
        visited = set()
        res = 0
        for char in password:
            if char in visited:
                continue
            asc = ord(char)
            if asc in range(97, 123):
                res += 1
            elif asc in range(65, 91):
                res += 2
            elif asc in range(48, 58):
                res += 3
            else:
                res += 5
            visited.add(char)
        return res
