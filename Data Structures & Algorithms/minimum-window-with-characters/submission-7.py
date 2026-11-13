class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        res_len = float("infinity")
        res_indices = -1, -1
        cmap_t = {}
        cmap_s = {}
        freq_matched = 0

        for c in t:
            cmap_t[c] = 1 + cmap_t.get(c, 0)
            
        l = 0
        for r in range(len(s)):
            if s[r] in cmap_t:
                cmap_s[s[r]] = 1 + cmap_s.get(s[r], 0)
                if cmap_s[s[r]] == cmap_t[s[r]]:
                    freq_matched += 1
        
            if freq_matched == len(cmap_t):
                while l <= r:
                    if s[l] in cmap_t and cmap_s[s[l]] == cmap_t[s[l]]:
                        break
                    elif s[l] in cmap_t:
                        cmap_s[s[l]] -= 1
                    l += 1
            
                if (r-l+1) < res_len:
                    res_len = r-l+1
                    res_indices = l, r+1

                if s[l] in cmap_t:
                    cmap_s[s[l]] -= 1
                    if cmap_s[s[l]] < cmap_t[s[l]]:
                        freq_matched -= 1
                l += 1
                

        if res_indices[0] == -1:
            return ""        

        return s[res_indices[0]:res_indices[1]]    