class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a - z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            ans[tuple(count)].append(s)
        
        return ans.values()
    
# class Solution: # with sorting
#     def groupAnagrams(self, strs):
#         anagram_map = defaultdict(list)
        
#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             anagram_map[sorted_word].append(word)
        
#         return list(anagram_map.values())