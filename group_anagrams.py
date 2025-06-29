"""
https://leetcode.com/problems/group-anagrams/

Edge cases:
1. Only one string

Time Complexity: O(nklogk)
Space Complexity: O(nk)
The number of words n. The length of the words is k. So it’s O(nk).
You store entire strings (of length k) as: Dict keys (tuples or joined strings), Dict values (lists of words). Each word takes O(k) space --> n such words → O(nk)
"""

class Solution:
  def groupAnagrams(self, strs):
    groupMap = {}
    
    #Pythonic using defaultdict from collections. d = defaultdict(list) --> If a key doesn’t exist yet, automatically create it with an empty list as the default value.
    for word in strs:
      # sorts the characters of string and returns them in a list. So join them as a string. --> "sorted(eat)" --> ['a', 'e', 't']
      newKey = ''.join(sorted(word)) # O(klogk) where k is the avg length of the string
      if newKey in groupMap:
        groupMap[newKey].append(word)
      else:
        groupMap[newKey] = [word]
    return list(groupMap.values()) # returns a dict view which not printable but can be used in loops, so convert to a string.
  
strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))