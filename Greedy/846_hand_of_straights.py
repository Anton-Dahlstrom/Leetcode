from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        array = [[0, groupSize] for _ in range(0, (len(hand)//groupSize))]
        for card in hand:
            found = False
            for i in range(0, len(array)):
                val, free = array[i]
                if not free:
                    continue
                if free == groupSize or val == card-1:
                    array[i][0] = card
                    array[i][1] -= 1
                    found = True
                    break
            if not found:
                return False
        return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
output = True

hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
output = True

obj = Solution()
res = obj.isNStraightHand(hand, groupSize)
print(res)
