class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        s_dict = {}
        t_dict = {}
        res = ""
        min_seq = len(s)

        for c in t:
            t_dict[c] = 1 + t_dict.get(c, 0)

        l=0
        for r in range(len(s)):
            if s[r] in t_dict:
                s_dict[s[r]] = 1 + s_dict.get(s[r], 0)    

            while l < r:
                if s[l] not in t_dict:
                    l += 1
                else:
                    if s_dict[s[l]] <= t_dict[s[l]]: 
                        break   
                    s_dict[s[l]] -= 1
                    l += 1

            isvalid = True
            for k in t_dict:
                if s_dict.get(k,0) < t_dict[k]:
                    isvalid = False


            if isvalid:
                if min_seq >= r-l+1:
                    min_seq = r-l+1
                    res = s[l:r+1]
                if s[l] in t_dict:
                    s_dict[s[l]] -=1
                l += 1
                
        return res