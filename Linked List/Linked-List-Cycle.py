# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast = head # slow and fast pointer approach (also called hare and tortoise approach)
        # while fast and fast.next:
        #     head, fast = head.next, fast.next.next
        #     if head is fast:
        #         return True
        # return False
        
        di, i = {}, 0 # dictionary approach
        while head:
            if head in di: return True
            else: di[head] = i
            i += 1
            head = head.next
        return False