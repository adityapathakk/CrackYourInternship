# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = head.val # binary representation
        while head.next:
            ans = 2 * ans + head.next.val
            head = head.next
        return ans

        # ans = head.val # bit manipulation
        # while head.next:
        #     ans = (ans << 1) | head.next.val
        #     head = head.next
        # return ans