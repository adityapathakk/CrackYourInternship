class Solution:
    def check(self, root, low, high, count):
        if not root:
            return 0
            
        if low <= root.data <= high:
            count[0] += 1
        
        self.check(root.left, low, high, count)
        self.check(root.right, low, high, count)
        
    def getCount(self, root, low, high):
        count = [0]
        self.check(root, low, high, count)
        return count[0]