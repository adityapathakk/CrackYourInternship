class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        arr.sort()
        res = 1
        
        for elem in arr:
            if res == elem:
                res += 1
        
        return res