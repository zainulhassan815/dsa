# https://leetcode.com/problems/odd-even-linked-list
# 328. Odd Even Linked List

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if (not head) or (not head.next) or (not head.next.next):
        return head

    start = head
    odd = head
    even = head.next
    even_start = even

    while odd.next and even.next:
        odd.next = odd.next.next
        odd = odd.next

        if even.next.next:
            even.next = even.next.next
            even = even.next

    even.next = None
    odd.next = even_start

    return start
