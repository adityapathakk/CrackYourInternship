class Solution:
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		v = [(nums[i], i) for i in range(len(nums))]
		v.sort()
		cnt, i = 0, 0
		
		while i < len(nums):
			index = v[i][1]
			if i != index:
					cnt += 1
					v[i], v[index] = v[index], v[i]
					i -= 1
			i += 1
	        
		return cnt