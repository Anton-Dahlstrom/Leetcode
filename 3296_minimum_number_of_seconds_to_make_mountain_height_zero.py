
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        n = len(workerTimes)

        # Brute force to see if the mountain can be erased in the allowed amount of seconds.
        def eraseMountain(allowedSeconds):
            height = mountainHeight
            for i in range(n):
                seconds = 0
                j = 1
                # This part can be sped up with better math.
                while height > 0:
                    seconds += j*workerTimes[i]
                    if seconds <= allowedSeconds:
                        height -= 1
                        j += 1
                        continue
                    break

                if height <= 0:
                    return True
            return False

        l = 1
        # The way we choose for r can be improved.
        r = (mountainHeight*min(workerTimes)) ** 3
        # Binary search that finds the lowest amount of seconds that is able to erase the mountain
        while l < r:
            mid = l + ((r-l)//2)
            if not eraseMountain(mid):
                l = mid+1
            else:
                r = mid
        return r


mountainHeight = 4
workerTimes = [2, 1, 1]
output = 3


obj = Solution()
res = obj.minNumberOfSeconds(mountainHeight, workerTimes)
print(res)
print(output)
print(res == output)
