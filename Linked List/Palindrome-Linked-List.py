# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str1 = str2 = ""
        node = head

        while node is not None:
            str1 = str1 + str(node.val)
            str2 = str(node.val) + str2
            node = node.next
        
        return str1 == str2

        # a = []
        # while head:
        #     a.append(head.val)
        #     head = head.next
        # return a == a[::-1]

# from collections import deque
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         deq = deque()

#         while head:
#             deq.append(head.val)
#             head = head.next
        
#         if len(deq) == 1:
#             return True

#         while len(deq) > 1:
#             if deq.popleft() != deq.pop():
#                 return False
        
#         return True