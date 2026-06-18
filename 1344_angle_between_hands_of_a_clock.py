class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        minutes %= 60

        minutes *= 30
        minutes //= 5

        hour *= 30
        hour += (minutes / 12)

        diff = abs(hour-minutes)
        res = min(360-diff, diff)
        return res
