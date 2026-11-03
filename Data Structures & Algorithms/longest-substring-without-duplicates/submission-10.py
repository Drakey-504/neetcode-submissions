class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        char_map = {}

        l = 0
        for r in range(0,len(s)):
            char_map[s[r]] = 1 + char_map.get(s[r], 0)

            while l < r and char_map.get(s[r], 0) > 1:
                char_map[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)    
        
        return res