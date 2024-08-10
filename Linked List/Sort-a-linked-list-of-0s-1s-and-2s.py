# also read this https://www.geeksforgeeks.org/how-to-sort-a-linked-list-that-is-sorted-alternating-ascending-and-descending-orders/

class Node:
      # Constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to sort a linked list of 0s, 1s and 2s
def sort_list(head):
    # Initialize count of '0', '1' and '2' as 0
    cnt = [0, 0, 0]
    ptr = head

    # Traverse and count total number of '0', '1' and '2'. cnt[0] will store total number of '0's.
    # cnt[1] will store total number of '1's. cnt[2] will store total number of '2's
    while ptr is not None:
        cnt[ptr.data] += 1
        ptr = ptr.next

    idx = 0
    ptr = head
    
    # Fill first cnt[0] nodes with value 0. Fill next cnt[1] nodes with value 1. Fill remaining cnt[2] nodes with value 2
    while ptr is not None:
        if cnt[idx] == 0:
            idx += 1
        else:
            ptr.data = idx
            cnt[idx] -= 1
            ptr = ptr.next