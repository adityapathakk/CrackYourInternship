from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        return list(sorted(set(permutations(arr))))
        
# from typing import List
# class Solution:
#     def uniquePerms(self, arr: List[int], n: int) -> List[List[int]]:
#         def backtrack(path, remaining):
#             if not remaining:
#                 # Convert the tuple to a list and add it to the result
#                 result.append(list(path))
#                 return
            
#             for i in range(len(remaining)):
#                 # To avoid duplicates, skip the number if it's the same as the previous one and we haven't used it
#                 if i > 0 and remaining[i] == remaining[i - 1]:
#                     continue
                
#                 # Include remaining[i] in the current path and recursively generate the rest
#                 backtrack(path + (remaining[i],), remaining[:i] + remaining[i+1:])
        
#         # Sort the array to make sure duplicates are adjacent
#         arr.sort()
#         result = []
#         # Call backtrack with an empty path and the sorted array
#         backtrack((), arr)
#         return result