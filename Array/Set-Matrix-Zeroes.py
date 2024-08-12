class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
# whenever j and i aren't equal, it means a unique element is found. so length of unique elements' list increases.
                nums[j] = nums[i]
        
        return j + 1 # j began from the 0th index.

# also, we could simply use the property of lists:
        #nums[:] = sorted(set(nums))
        #return len(nums)