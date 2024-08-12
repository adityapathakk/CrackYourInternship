# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newCurr, oldCurr = None, head
        while oldCurr:
            temp = oldCurr.next
            oldCurr.next = newCurr 
            newCurr = oldCurr 
            oldCurr = temp  
        return newCurr