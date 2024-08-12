# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        mod = (10 ** 9) + 7
        num1 = num2 = 0
        while first:
            num1 = ((num1 * 10) % mod) + first.data
            first = first.next
        while second:
            num2 = ((num2 * 10) % mod) + second.data
            second = second.next
        return (num1 * num2) % mod