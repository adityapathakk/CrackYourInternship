# this is tough, revise this from solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Base Case: If the length of the linked list is less than or equal to 1, then the list is already sorted
        if not head or not head.next:
            return head

        # Split the linked list into two halves using "slow and fast pointer" technique to find the midpoint of the linked list
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # The midpoint of the linked list is slow.next
        mid = slow.next
        
        # Set slow.next to None to separate the left and right halves of the linked list
        slow.next = None

        # Recursively sort the left and right halves of the linked list
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves of the linked list
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        # Append the remaining nodes of the left or right half to the end of the sorted list
        curr.next = left or right

        return dummy.next
        
        # dummy = ListNode(0) # [Optimised Solution - TC O(nlogn), SC O(1)]
        # dummy.next = head

        # # Grab sublists of size 1, then 2, then 4, etc, until fully merged
        # steps = 1
        # while True:
        #     # Record the progress of the current pass into a single semi sorted list by updating
        #     # the next of the previous node (or the dummy on the first loop)
        #     prev = dummy

        #     # Keep track of how much is left to process on this pass of the list
        #     remaining = prev.next

        #     # While the current pass though the list has not been completed
        #     num_loops = 0
        #     while remaining:
        #         num_loops += 1

        #         # Split 2 sublists of steps length from the front
        #         sublists = [None, None]
        #         sublists_tail = [None, None]
        #         for i in range(2):
        #             sublists[i] = remaining
        #             substeps = steps
        #             while substeps and remaining:
        #                 substeps -= 1
        #                 sublists_tail[i] = remaining
        #                 remaining = remaining.next
        #                 # Ensure the subslist (if one was made) is terminated
        #             if sublists_tail[i]:
        #                 sublists_tail[i].next = None

        #     # We have two sublists of (upto) length step that are sorted, merge them onto 
        #     # the end into a single list of (upto) step * 2
        #         while sublists[0] and sublists[1]:
        #             if sublists[0].val <= sublists[1].val:
        #                 prev.next = sublists[0]
        #                 sublists[0] = sublists[0].next
        #             else:
        #                 prev.next = sublists[1]
        #                 sublists[1] = sublists[1].next
        #             prev = prev.next
            
        #     # One list has been finished, attach what ever is left of the other to the end
        #         if sublists[0]:
        #             prev.next = sublists[0]
        #             prev = sublists_tail[0]
        #         else:
        #             prev.next = sublists[1]
        #             prev = sublists_tail[1]
            
        #     # Double the steps each go around
        #     steps *= 2

        #     # If the entire list was fully processed in a single loop, it means we've completely sorted the list and are done
        #     if 1 >= num_loops: return dummy.next