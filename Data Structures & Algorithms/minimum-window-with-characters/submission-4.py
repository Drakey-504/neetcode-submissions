class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""


        s_freq = {}
        t_freq = {}
        freq_match = 0
        res_indexes = (-1,-1)
        min_seq = len(s)

        for i in range(len(t)):
            t_freq[t[i]] = 1 + t_freq.get(t[i], 0)

        l=0
        for r in range(len(s)):

            if s[r] in t_freq:
                s_freq[s[r]] = 1 + s_freq.get(s[r], 0)
                
                if s_freq[s[r]] == t_freq[s[r]]:
                    freq_match += 1

            while l < r:
                if s[l] in t_freq:
                    if s_freq[s[l]]-1 < t_freq[s[l]]:
                        break
                    s_freq[s[l]] -= 1    
                l += 1
            if freq_match == len(t_freq):
                if min_seq >= r-l+1:
                    res_indexes = (l,r)
                    min_seq = r-l+1
                if s[l] in t_freq:
                    s_freq[s[l]] -= 1
                    if s_freq[s[l]] < t_freq[s[l]]:  
                        freq_match -= 1
                l += 1          
        if res_indexes[0] == -1:
            return ""
        else:
            return s[res_indexes[0]:res_indexes[1]+1]                 






