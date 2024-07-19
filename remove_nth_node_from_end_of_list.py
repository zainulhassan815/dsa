# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# 19. Remove Nth Node From End of List

from typing import Optional


class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)

    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        right = right.next
        left = left.next

    left.next = left.next.next

    return dummy.next
