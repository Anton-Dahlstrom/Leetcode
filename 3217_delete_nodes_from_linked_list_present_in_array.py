from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode()
        cur = head
        tail = dummy
        while cur:
            print(cur.val, cur.val in nums)
            if cur.val not in nums:
                tail.next = cur
                tail = cur
            cur = cur.next
        tail.next = None
        return dummy.next
