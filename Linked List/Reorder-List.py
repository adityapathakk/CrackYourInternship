# revise from here: https://leetcode.com/problems/reorder-list/solutions/801971/python-o-n-by-two-pointers-w-visualization
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head: # base case
            return None

        # locate the mid point of linked list
        # first half is the linked list before mid point
        # second half is the linked list after mid point
        
        fast, slow = head, head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        mid = slow

        # reverse second half
        
        prev, cur = None, mid
        
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        head_of_second_rev = prev

        # update link between first half and reversed second half
        
        first, second = head, head_of_second_rev
        
        while second.next:
            
            next_hop = first.next
            first.next = second
            first = next_hop
            
            next_hop = second.next
            second.next = first
            second = next_hop