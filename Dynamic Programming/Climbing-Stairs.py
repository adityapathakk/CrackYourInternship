class Solution:
    def climbStairs(self, n: int) -> int:
        if n in {0, 1}:
            return 1
        
        prev, curr = 1, 1
        for _ in range(2, n + 1):
            prev, curr = curr, curr + prev
        return curr