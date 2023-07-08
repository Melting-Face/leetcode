# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        length = 0
        while head:
            arr.append(head)
            head = head.next
            length += 1
        return arr[math.floor(length / 2)]
        