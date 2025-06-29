"""
https://leetcode.com/problems/isomorphic-strings/description/

Edge cases:
1. unequal length
2. Both strings of length 1
3. Both strings of length 0

Solution 1: 2 hashmaps.

Solution 2: 1 hashmap and 1 hashset.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 1 or len(t) == 0:
            return True
    
        s_to_t = {}
        check = []
    
        for c1, c2 in zip(s,t):
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            else:
                if c2 in check:
                    return False
                s_to_t[c1] = c2
                check.append(c2)
        return True



Time Complexity: O(n) where n is the length of strings s, t
Space Complexity: O(2n) ~ O(n) where n is the length of strings s, t
"""
class Solution:
  def isIsomorphic(self, s, t): # Python (PEP-8) suggests PascalCase for classes, and not camelCase.
    if len(s) == 1 or len(t) == 0: # contraint is that len(s) == len(t) always so don't need to check if   both s and t are of equal length.
      return True
    
    s_to_t = {}
    t_to_s = {}
    
    for c1, c2 in zip(s,t): # mapping characters in s and t
    # instead of zip() 
    # for i in range(len(s)):
    # c1 = s[i]
    # c2 = t[i] 
      if c1 in s_to_t:
        if s_to_t[c1] != c2:
          return False
      else:
        s_to_t[c1] = c2
        
      if c2 in t_to_s:
        if t_to_s[c2] != c1:
          return False
      else:
        t_to_s[c2] = c1
        
    return True
  
s = "foo"
t = "bar"
sol = Solution()
print(sol.isIsomorphic(s, t))
          
          

    
    
    
    