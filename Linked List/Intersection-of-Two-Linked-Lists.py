# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one, two = headA, headB

        while one != two:
            one = headB if not one else one.next
            two = headA if not two else two.next

        return one