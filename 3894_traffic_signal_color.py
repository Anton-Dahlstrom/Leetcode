class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if timer in range(31, 91):
            return "Red"
        return "Invalid"
