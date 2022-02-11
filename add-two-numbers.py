# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digitStack = []
        carry = 0
        node = ListNode()
        node_tail  = node
        #output = null
        while l1 or l2 or carry:
            #first list
            a = l1.val if l1 else 0 
            b = l2.val if l2 else 0
            
            digit = (a+b+carry)%10    
            carry = math.floor((a+b+carry)/10)
            node_tail.next = ListNode(digit)
            node_tail = node_tail.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            #digitStack.append(digit)
               
#         if carry:
#             digitStack.append(carry)
            
#         while digitStack:
#             val = digitStack.pop(0)
#             output.next = ListNode(val)
#             output = output.next
        return node.next
            
