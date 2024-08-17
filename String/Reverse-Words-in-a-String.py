class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = ""
        
        for i in range(len(s)):
            if i == len(s) - 1:
                ans = str(s[i]) + ans
            else:
                ans = " " + str(s[i]) + ans

        return ans

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         x = s.split()
#         x = x[::-1]
#         return ' '.join(x)

# class Solution: # without using split or join
#     def reverseWords(self, s: str) -> str:
#         words = []

#         curr_word = ''

#         for c in s + ' ':  # Append a space to also get last word
#             if c != ' ':
#                 curr_word += c 
#             elif len(curr_word):
#                 words.append(curr_word)
#                 curr_word = ''

#         ans = ''

#         for i in range(len(words) - 1, -1, -1):
#             ans += words[i]
            
#             if i > 0:
#                 ans += ' '
        
#         return ans