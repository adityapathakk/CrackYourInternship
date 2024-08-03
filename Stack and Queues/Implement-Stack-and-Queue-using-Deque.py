# Link to problem: https://www.geeksforgeeks.org/problems/deque-implementations/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

#dq : deque in which element is to be pushed
#x : element to be pushed

# function to push element x to the front of the deque.
def push_front_pf(dq,x):
    dq.appendleft(x)
    
# function to push element x to the back of the deque.
def push_back_pb(dq,x):
    dq.append(x)
    
# function to return element from front of the deque.
def front_dq(dq):
    if not dq: return -1
    return dq[0]
    
# function to pop element from back of the deque.
def pop_back_ppb(dq):
    if dq: dq.pop()

# class node:
#     def __init__(self,val):
#         self.val = val
#         self.prev = None
#         self.next = None
    
# class Deque:
#     def __init__(self):
#         self.head = self.tail = None
    
#     def isEmpty(self):
#         if (self.head == None): return True
#         return False
    
#     def insert_first(self,element):
#         newP = node(element)
#         if self.head == None: 
#             self.head = self.tail = newP
#             return
#         newP.next = self.head
#         self.head.prev = newP
#         self.head = newP
    
#     def insert_last(self,element):
#         newP = node(element)
#         if self.head == None: 
#             self.head = self.tail = newP
#             return
#         newP.prev = self.tail
#         self.tail.next = newP
#         self.tail = newP
        
#     def size(self):
#         curr = self.head
#         len = 0
#         while curr != None:
#             len += 1
#             curr = curr.next
#         return len
        
#     def remove_first(self):
#         if self.isEmpty(): 
#             print('list is empty')
#             return
#         self.head = self.head.next
#         if self.head != None: self.head.prev = None
        
#     def remove_last(self):
#         if self.isEmpty():
#             print('list is empty')
#             return
#         self.tail =  self.tail.prev
#         if self.tail != None: self.tail.next = None
        
#     def display(self):
#         if self.isEmpty():
#             print('list is empty')
#             return
#         curr = self.head
#         while curr != None:
#             print(curr.val,end = ' ')
#             curr = curr.next
#         print()
            
# class Stack:
#     def __init__(self):
#         self.stack = Deque()
    
#     def push(self,element):
#         self.stack.insert_last(element)
    
#     def pop(self):
#         self.stack.remove_last()
        
#     def size(self):
#         return self.stack.size()
    
#     def display(self):
#         self.stack.display()
        
# class Queue:
#     def __init__(self):
#         self.que = Deque()
    
#     def enqueue(self,element):
#         self.que.insert_last(element)
    
#     def dequeue(self):
#         self.que.remove_first()
        
#     def size(self):
#         return self.que.size()
        
#     def display(self):
#         self.que.display()
                
# stk = Stack() 

#  # push 7 and 8 at top of stack
# stk.push(7) 
# stk.push(8) 
# print("Stack: ") 
# stk.display() 

# # pop an element
# stk.pop() 
# print("Stack: ") 
# stk.display() 

# # object of queue
# que = Queue() 

# # insert 12 and 13 in queue
# que.enqueue(12) 
# que.enqueue(13) 
# print("Queue: ") 
# que.display() 

# # delete an element from queue
# que.dequeue() 
# print("Queue: ") 
# que.display() 

# print("Size of stack is ",stk.size()) 
# print("Size of queue is ", que.size()) 