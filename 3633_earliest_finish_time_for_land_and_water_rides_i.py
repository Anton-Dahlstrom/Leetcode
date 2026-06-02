from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float("inf")
        for i in range(len(landStartTime)):
            ls, le = landStartTime[i], landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                ws, we = waterStartTime[j], waterStartTime[j] + \
                    waterDuration[j]
                res = min(res, max(le, ws) + waterDuration[j])
                res = min(res, max(we, ls) + landDuration[i])
        return res
