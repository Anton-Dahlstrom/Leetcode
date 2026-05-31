from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        n = len(asteroids)
        for i in range(n):
            if mass >= asteroids[i]:
                mass += asteroids[i]
            else:
                return False
        return True
