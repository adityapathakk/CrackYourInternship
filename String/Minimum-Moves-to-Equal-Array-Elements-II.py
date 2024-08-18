class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid, res = nums[len(nums) // 2], 0
        
        for i in nums:
            res += abs(mid - i)
            
        return res