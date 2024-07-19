# https://leetcode.com/problems/reverse-linked-list/
# 206. Reverse Linked List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, current = None, head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev
