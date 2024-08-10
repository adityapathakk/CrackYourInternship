# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        currNode = dummyHead
        
        while currNode.next:
            if currNode.next.val == val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next
        
        return dummyHead.next