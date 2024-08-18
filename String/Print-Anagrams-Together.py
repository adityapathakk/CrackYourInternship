from collections import defaultdict
class Solution:
    def Anagrams(self, words, n):
        ans = defaultdict(list)

        for s in words:
            count = [0] * 26 # a - z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            ans[tuple(count)].append(s)
        
        return ans.values()