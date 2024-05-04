# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        upbit = 0
        values = []
        while l1 or l2:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            val = l1_value + l2_value + upbit
            upbit = 0
            if val >= 10:
                val -= 10
                upbit = 1
            values.append(val)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if upbit:
            values.append(upbit)
        list_node = None
        for value in values[::-1]:
            list_node = ListNode(val=value, next=list_node)
        return list_node
        
            
#         while l1_value or l2_value:
#             l1_value + l2_value + upbit
            
#             l1_value = l1.val
#             l2_value = l2.val
#             l1 = l1.next
#             l2 = l2.next
        