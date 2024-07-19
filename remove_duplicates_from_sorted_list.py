# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# 83. Remove Duplicates from Sorted List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head

    while current:
        while current.next and current.next.val == current.val:
            current.next = current.next.next
        current = current.next
    return head
