"""
https://leetcode.com/problems/word-pattern/description/ (similar to isomorphic strings)

Edge cases:
1. Only one string in s and 1 character in pattern.
2. Pattern and s have different lengths

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
  def wordPattern(self, pattern, s):
    if len(s.split()) != len(pattern): #len(s.split()) --> length of string without spaces
      return False
    
    if len(s.split()) == len(pattern) == 1:
      return True
    
    s_list = s.split() # O(len(s)) → O(n * k) in worst case
    patternMap= {}
    sMap = {}
    
    for i in range(len(pattern)):
      c1 = pattern[i]
      c2 = s_list[i]
      
      if c1 in patternMap:
        if patternMap[c1] != c2:
          return False
      else:
        patternMap[c1] = c2
        
      if c2 in sMap:
        if sMap[c2] != c1:
          return False
      else:
        sMap[c2] = c1
    return True
  
pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
print(sol.wordPattern(pattern, s))