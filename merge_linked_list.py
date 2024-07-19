# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    p1, p2 = list1, list2

    while p1 and p2:
        if p1.val < p2.val:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next

        current = current.next

    if p1:
        current.next = p1
    elif p2:
        current.next = p2

    return dummy.next
