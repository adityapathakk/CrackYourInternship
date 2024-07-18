class Solution: # my solution using a set to store visited elements
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for i in (nums):
            if i in visited:
                return i
            visited.add(i)

''' Hare & Tortoise Method - Most Optimal - O(N) Time, O(1) Memory

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast

'''
