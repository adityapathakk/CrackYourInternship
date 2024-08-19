'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
'''
class Solution:
    def compute(self,head):
        curr, prev, nextt = head, None, None

        while (curr is not None): # reversing linked list
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        head = prev
        current = head
        maxNode = head
        temp = None

        # removing nodes which are smaller than the current maximum node
        while (current is not None and current.next is not None):
            if current.next.data < maxNode.data:
                temp = current.next
                current.next = temp.next
            else:
                current = current.next
                maxNode = current
        curr = head
        prev = None

        # reversing the linked list again and updating the head
        while (curr is not None):
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head = prev
        return head