class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l,r = 0,0
        res = 0

        char_set = {}

        while r < len(s):
            char_set[s[r]] = 1 + char_set.get(s[r], 0)
            if char_set[s[r]] > 1:
                while char_set[s[r]] > 1:
                    char_set[s[l]] -= 1
                    l += 1
            res = max(res, r-l+1)
            r +=1        

        return res    
        