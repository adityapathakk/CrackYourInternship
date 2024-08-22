# revise from here: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/1037986/python-two-pointer-solution-with-comments-easy-to-understand
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head

        # advance fast to nth position
        for _ in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
        
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # delete the node
        slow.next = slow.next.next
        return head