from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        n = len(arr)
        res = float("-inf")
        for i in range(n//2):
            res = max(res, arr[i]+arr[n-i-1])
        return res
