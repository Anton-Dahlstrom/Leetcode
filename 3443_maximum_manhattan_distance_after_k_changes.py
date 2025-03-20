class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        prefix = [0] * 4
        best = 0
        res = 0
        # If we change a directions before a peak distance we can add 2 to the peak distance.
        # Otherwise we can add 1.
        for i, direction in enumerate(s):
            if direction == "N":
                prefix[0] += 1
                prefix[1] += 1
                prefix[2] -= 1
                prefix[3] -= 1
            elif direction == "S":
                prefix[0] -= 1
                prefix[1] -= 1
                prefix[2] += 1
                prefix[3] += 1
            elif direction == "W":
                prefix[0] += 1
                prefix[1] -= 1
                prefix[2] -= 1
                prefix[3] += 1
            elif direction == "E":
                prefix[0] -= 1
                prefix[1] += 1
                prefix[2] += 1
                prefix[3] -= 1

            best = max(prefix)
            # We change as many moves before our peak as possible.
            prevChanges = min(k, i-best+1) * 2
            # The rest of our available k's are used for direction changes after the peak
            futureChanges = max(0, k - prevChanges)
            tempk = k
            tempk -= i-best + 1
            res = min(
                i+1, max(res, best + prevChanges + futureChanges))
        return res


s = "SNWWEEW"
k = 2
output = 5

obj = Solution()
res = obj.maxDistance(s, k)
print(res)
print(output)
print(res == output)
