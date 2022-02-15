from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base condition
        if s == "":
            return 0
        
        maxLength = 0
        unique = set()
        start, end = 0, 0
        
        while end < len(s):
            if s[end] not in unique:
                unique.add(s[end])
                end+=1
                maxLength = max(maxLength, len(unique))
            else:
                unique.remove(s[start])
                start +=1
        
        return maxLength
