# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], [] # 2 stacks approach

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        res, carry = None, 0

        while s1 or s2 or carry:
            d1 = s1.pop() if s1 else 0
            d2 = s2.pop() if s2 else 0

            s = d1 + d2 + carry
            d, carry = s % 10, s // 10

            newNode = ListNode(d)
            newNode.next = res
            res = newNode
        
        return res
        
        # s1, s2 = 0, 0 # very easy approach

        # while l1:
        #     s1 = s1 * 10 + l1.val
        #     l1 = l1.next
        
        # while l2:
        #     s2 = s2 * 10 + l2.val
        #     l2 = l2.next

        # dummyHead = ListNode(0)
        # l3 = dummyHead

        # for i in str(s1 + s2):
        #     l3.next = ListNode(i)
        #     l3 = l3.next

        # return dummyHead.next